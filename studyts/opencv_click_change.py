import cv2
import numpy as np

points=[]

globals 

def draw_rect(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        cv2.rectangle(img,(x,y),(x+50,y+50),(255,0,0),-1)
        for coord in points:
            print(coord)    
        if len(points) == 4:
            cv2.destroyWindow('image')

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rect)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1)&0xff==27:
        break
cv2.destroyAllWindows()

