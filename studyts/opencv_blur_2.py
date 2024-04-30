import cv2
import numpy as np
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("./images/img8.jpg",cv2.IMREAD_GRAYSCALE)

if img1 is None:
    print("no file found")
    exit()

ksize1 = 7; ksize2 = 9
res1 = cv2.GaussianBlur(img1, (ksize1,ksize1),0)
res2 = cv2.GaussianBlur(img1, (ksize2,ksize2),0)
res3 = cv2.GaussianBlur(img1, (1,21),0)

ress = []
ress.append(img1), ress.append(res1), 
ress.append(res2), ress.append(res3)

titles = ['input','7*7','9*9','1*21']

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(ress[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()