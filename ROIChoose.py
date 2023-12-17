import cv2
import numpy as np

ROIPoints = np.array([[-500, 85], [-500, 82], [-500, 338], [-500, 341]])
#ROIPoints = np.array([[100, 85], [427, 82], [441, 338], [88, 341]])

homography, status, ROIDestination = None, None, None

is_mouse_was_pressed = False

def mouselogic(event, x, y, flags,param):
    global ROIPoints
    if event == cv2.EVENT_LBUTTONDOWN:
        global is_mouse_was_pressed
        if not is_mouse_was_pressed:
            for i in range(0, 4):
                if ROIPoints[i][0] == -500:
                    ROIPoints[i][0] = x
                    ROIPoints[i][1] = y
                    break
            print(ROIPoints)
        is_mouse_was_pressed = True
    if event == cv2.EVENT_LBUTTONUP:
        is_mouse_was_pressed = False

def init(frame, work_dimensions, camera_num = 1):
    global ROIDestination
    ROIDestination = np.array([[0, 0], [work_dimensions[0], 0], work_dimensions, [0, work_dimensions[1]]])
    cv2.imshow("ChooseROIPoints", frame)
    cv2.setMouseCallback('ChooseROIPoints', mouselogic)

def update(frame):
    for i in range(0, 4):
        cv2.circle(frame, ROIPoints[i], 3, (i * 150, (i + 1) * 150, (i + 2) * 150), 2)
    cv2.imshow("ChooseROIPoints", frame)

def finish():
    global homography, status
    if ROIChoosed():
        homography, status = cv2.findHomography(ROIPoints, ROIDestination)
        cv2.destroyWindow("ChooseROIPoints")
        #f = open('ROICords', 'w', encoding="utf-8")

def ROIChoosed():
    return ROIPoints[0][0] != -500 and ROIPoints[1][0] != -500 and ROIPoints[2][0] != -500 and ROIPoints[3][0] != -500