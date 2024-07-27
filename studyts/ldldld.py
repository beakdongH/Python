import cv2
import numpy as np

def onChange(trackbarValue):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Webcam with Filter")
cv2.createTrackbar("Filter Size", "Webcam with Filter", 1, 20, onChange)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    filterSize = cv2.getTrackbarPos("Filter Size", "Webcam with Filter")

    if filterSize == 0:
        filterSize = 1

    frame_filtered = cv2.GaussianBlur(frame, (filterSize * 2 + 1, filterSize * 2 + 1), 0)
    
    cv2.imshow("Webcam with Filter", frame_filtered)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()