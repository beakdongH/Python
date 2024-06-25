import cv2
import numpy as np

click = False
click2 = False
x1, y1 = -1, -1
x2, y2 = -1, -1

def mousePass(event, x, y, flags, param):
    pass

def mouseCallback(event, x, y, flags, param):
    global x1, y1, x2, y2, click, click2, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        click = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if click:
            frame = frameCp.copy()
            cv2.rectangle(frame, (x1, y1), (x, y), (255, 0, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if click:
            x2, y2 = x, y
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            click2 = True

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

if not cam.isOpened():
    print('Webcam error')
    exit()

cv2.namedWindow("test")
cv2.setMouseCallback("test", mouseCallback)

status, frame = cam.read()
frameCp = frame.copy()

while not click2:
    cv2.imshow("test", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if click2:
        break

cv2.imshow("test", frame)
cv2.setMouseCallback("test", mousePass)
cv2.namedWindow("template")
template2 = frame[y1:y2, x1:x2]
cv2.imshow("template", template2)
cv2.waitKey(10)

w = x2 - x1
h = y2 - y1
methods = cv2.TM_CCOEFF_NORMED

while cam.isOpened():
    status, frame = cam.read()
    rows, cols = frame.shape[:2]
    res = cv2.matchTemplate(frame, template2, methods)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    M = np.float64([[1, 0, -max_loc[0] + int(-w/2 + cols/2)], 
                    [0, 1, -max_loc[1] + int(-h/2 + rows/2)]])
    dst = cv2.warpAffine(frame, M, (cols, rows))
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    if status:
        cv2.imshow("test", dst)
        # cv2.imshow("test", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
