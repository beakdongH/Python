import os 
import cv2

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print('Cannot open the camera-%d'%(CAMERA_ID))
    exit()

cv2.namedWindow('CAM Windows')
while True:
    ret, frame = cam.read()
    cv2.imshow('CAM Windows',frame)

    if cv2.waitKey(10)>0:
        break

cam.release()
cv2.destroyAllWindows()