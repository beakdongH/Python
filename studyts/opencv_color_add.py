import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('images/img1.jpg')
img2 = cv.imread('images/img2.jpg')

img3 = cv.add(img1,img2)

img4 = cv.addWeighted(img1,0.5,img2,0.5,0)

titles=['src','map','add','addweight']

img5 = [img1,img2,img3,img4]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(img5[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()