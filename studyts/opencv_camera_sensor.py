import numpy as np
import cv2 as cv
import glob

nCols = 9
nRows = 6

criteria = (cv.TERM_CRITERIA_EPS+cv.TermCriteria_MAX_ITER,30,0.001)

objp = np.zeros((nCols*nRows,3),np.float32)
objp[:,:2] = np.mgrid[0:nCols,0:nRows].T.reshape(-1,2)

objpoint = []
imgpoint = []
images = glob.glob("imgs\*.jpg")

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (nCols, nRows), None)
    # If found, add object points, image points (after refining them) if ret == True:
    if ret == True:
        objpoint.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoint.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (nCols, nRows), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)
cv.destroyAllWindows()

# 카메라 캘리브레이션
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoint, imgpoint, gray.shape[::-1], None, None)

# 이미지 읽기
img = cv.imread(images[0])
h, w = img.shape[:2]

# 최적화된 새 카메라 매트릭스 계산
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# 이미지 왜곡 보정
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# 이미지 자르기
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]

# 보정된 이미지 저장
cv.imwrite('calibresult1.png', dst)

