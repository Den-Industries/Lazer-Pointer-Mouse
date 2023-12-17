from pynput.mouse import Button, Controller
from datetime import datetime
import cv2
import numpy as np
import math

import HSVChangeChoose
import CameraSettingsChoose
import ROIChoose

mouse = Controller()

lazerdelay = datetime.now()

previous_point, current_point = None, None

def update(frame, work_dimensions, out_dimensions):
    im_dst = cv2.warpPerspective(frame, ROIChoose.homography, work_dimensions)
    cv2.imshow("Projected image", im_dst)

    im_dst = cv2.cvtColor(im_dst, cv2.COLOR_RGB2HSV)
    HSVrange = HSVChangeChoose.GetRange()
    mask = cv2.inRange(im_dst, HSVrange[0], HSVrange[1])
    cv2.imshow("Mask", mask)

    kernel = np.ones((15, 15), np.uint8)
    mask = cv2.dilate(mask, kernel)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    maxarea = 0
    maxindex = 0
    for i in range(len(contours)):
        tmparea = cv2.contourArea(contours[i])
        if maxarea < tmparea:
            maxarea = tmparea
            maxindex = i

    #print("MAX AREA: ", maxarea)
    global lazerdelay, previous_point, current_point
    if contours and maxarea >= 150:
        bb = cv2.boundingRect(contours[maxindex])
        max_loc = [int(bb[0] + bb[2] / 2), int(bb[1] + bb[3] / 2)]
        #print(max_loc)
        max_loc = [int((max_loc[0] / work_dimensions[0]) * out_dimensions[0]),
                   int((max_loc[1] / work_dimensions[1]) * out_dimensions[1])]
        # print(max_loc)
        mouse.position = max_loc
        # mouse.press(button=Button.left)
        if (datetime.now() - lazerdelay).microseconds * 0.001 > 500:
            lazerdelay = datetime.now()
            mouse.click(button=Button.left)

        # cv2.imshow("Final mask", mask)
        if previous_point == None:
            previous_point = max_loc
            current_point = max_loc
        else:
            previous_point = current_point
            current_point = max_loc
            if math.sqrt(math.pow(previous_point[0] - current_point[0], 2)
                         + math.pow(previous_point[1] - current_point[1], 2)) > 14:
                lazerdelay = datetime.now()

    else:
        previous_point = None
        current_point = None
        lazerdelay = datetime.now()