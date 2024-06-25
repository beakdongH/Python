import cv2
import numpy as np

# Haar-like setting
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Camera setting
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)

while cam.isOpened():
    status, frame = cam.read()
    if not status:
        break

    rows, cols = frame.shape[:2]
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frameGray, 1.2, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    flag = False
    for (x, y, w, h) in faces:
        center = [int(x + w / 2), int(y + h / 2)]
        M = np.float64([[1, 0, -center[0] + int(cols / 2)], [0, 1, -center[1] + int(rows / 2)]])
        dst = cv2.warpAffine(frame, M, (cols, rows))
        flag = True
        break
    
    if flag:
        cv2.imshow("test", dst)
    else:
        cv2.imshow("test", frame)
    
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
