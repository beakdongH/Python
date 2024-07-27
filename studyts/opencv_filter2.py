import cv2
CAMERA_ID = 0

def nothing(trackbarValue):
    pass

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print
    'Cannot open teh camer-%d' & (CAMERA_ID)
    exit()

winName='images'
cv2.namedWindow('CAM Window')

filtSize1 = 1
filtSize2 = 2
filtTrkBar1 = 'filter Size_hor'
filtTrkBar2 = 'filter Size_ver'
cv2.createTrackbar(filtTrkBar1,winName,1,30,nothing)
cv2.createTrackbar(filtTrkBar2,winName,1,30,nothing)
cv2.createTrackbar(filtTrkBar1,winName,1)


while(True):
    ret, frame = cam.read()
    if (ret==True):
        filtSize1 = cv2.getTrackbarPos(filtTrkBar1,winName)
        filtSize1 = cv2.getTrackbarPos(filtTrkBar2,winName)

    if (filtSize1==0):
        filtSize1=1
        cv2.setTrackbarPos(filtTrkBar1,winName,filtSize1)

    if (filtSize2==0):
        filtSize2=1
        cv2.setTrackbarPos(filtTrkBar2,winName,filtSize2)

    imgBlur = cv2.blur
cv2.namedWindow('RGB track bar')
cv2.createTrackbar('red color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('blue color', 'RGB track bar', 0, 255, nothing)

cv2.setTrackbarPos('red color', 'RGB track bar', 125)
cv2.setTrackbarPos('green color', 'RGB track bar', 125)
cv2.setTrackbarPos('blue color', 'RGB track bar', 125)

img = np.zeros([512, 512, 3], np.uint8)

while(1):
    redVal = cv2.getTrackbarPos('red color', 'RGB track bar')
    greenVal = cv2.getTrackbarPos('green color', 'RGB track bar')
    blueVal = cv2.getTrackbarPos('blue color', 'RGB track bar')
