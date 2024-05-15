# 관련 라이브러리 선언
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("./images/img11.jpg", cv2.IMREAD_GRAYSCALE)

# 이동 변환
h, w, = img1.shape
c_h = h//2; c_w = w//2
rot_mat1 = cv2.getRotationMatrix2D((c_w,c_h),45,1)
rot_mat2 = cv2.getRotationMatrix2D((c_w,c_h),-45,1)
res1 = cv2.warpAffine(img1,rot_mat1,(w,h))
res2 = cv2.warpAffine(img1,rot_mat2,(w,h))
res3 = cv2.rotate(img1,cv2.ROTATE_90_CLOCKWISE)
res4 = cv2.flip(img1,1)
res5 = cv2.flip(img1,-1)

# 결과 영상 출력
ress = []
ress.append(img1), ress.append(res1), ress.append(res2)
ress.append(res3), ress.append(res4), ress.append(res5)
titles = ['input', 'res1', 'res2', 'res3', 'res4', 'res5']

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()