import cv2
import numpy as np

import HSVChangeChoose
import CameraSettingsChoose
import ROIChoose
import ProjectionAndMouseLogic

work_dimensions = [960, 540]
out_dimensions = [1920, 1080]

camera_for_cap = 1

cap = cv2.VideoCapture(camera_for_cap)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)
cap.set(cv2.CAP_PROP_CONTRAST, 145)
cap.set(cv2.CAP_PROP_SATURATION, 255)
cap.set(cv2.CAP_PROP_EXPOSURE, -3)

mode = 0

okay, frame = cap.read()

HSVChangeChoose.execute()

#CameraSettingsChoose.execute()

ROIChoose.init(frame, work_dimensions, camera_for_cap)

while True:
    okay, frame = cap.read()

    if mode == 0:
        ROIChoose.update(frame)

    if mode == 1:
        ProjectionAndMouseLogic.update(frame, work_dimensions, out_dimensions)

    if cv2.waitKey(1) == 13 and mode == 0 and ROIChoose.ROIChoosed():
        ROIChoose.finish()
        mode = 1
        cap.set(cv2.CAP_PROP_EXPOSURE, -9)