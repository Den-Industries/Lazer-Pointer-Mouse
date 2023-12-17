import cv2
import numpy as np

def nothing(x):
    pass

hMin, sMin, vMin, hMax, sMax, vMax = 0, 0, 70, 350, 255, 255

def execute():
    cv2.namedWindow('ChooseHSVRange')
    # create trackbars for color change
    cv2.createTrackbar('HMin','ChooseHSVRange',0,359,nothing) # Hue is from 0-179 for Opencv2
    cv2.createTrackbar('SMin','ChooseHSVRange',0,255,nothing)
    cv2.createTrackbar('VMin','ChooseHSVRange',0,255,nothing)
    cv2.createTrackbar('HMax','ChooseHSVRange',0,359,nothing)
    cv2.createTrackbar('SMax','ChooseHSVRange',0,255,nothing)
    cv2.createTrackbar('VMax','ChooseHSVRange',0,255,nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('HMin', 'ChooseHSVRange', 0)
    cv2.setTrackbarPos('SMin', 'ChooseHSVRange', 0)
    cv2.setTrackbarPos('VMin', 'ChooseHSVRange', 70)
    cv2.setTrackbarPos('HMax', 'ChooseHSVRange', 350)
    cv2.setTrackbarPos('SMax', 'ChooseHSVRange', 255)
    cv2.setTrackbarPos('VMax', 'ChooseHSVRange', 255)

    global hMin, sMin, vMin, hMax, sMax, vMax
    hMin = cv2.getTrackbarPos('HMin', 'ChooseHSVRange')
    sMin = cv2.getTrackbarPos('SMin', 'ChooseHSVRange')
    vMin = cv2.getTrackbarPos('VMin', 'ChooseHSVRange')
    hMax = cv2.getTrackbarPos('HMax', 'ChooseHSVRange')
    sMax = cv2.getTrackbarPos('SMax', 'ChooseHSVRange')
    vMax = cv2.getTrackbarPos('VMax', 'ChooseHSVRange')

def GetRange():
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    return (lower, upper)