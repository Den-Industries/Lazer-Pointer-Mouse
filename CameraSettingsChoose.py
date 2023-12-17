import cv2

def nothing(x):
    pass

def execute():
    cv2.namedWindow('CameraSettings')
    cv2.resizeWindow('CameraSettings', (660, 350))
    cv2.createTrackbar('Brightness','CameraSettings',0,255,nothing)
    cv2.createTrackbar('Contrast','CameraSettings',0,255,nothing)
    cv2.createTrackbar('Saturation','CameraSettings',0,255,nothing)
    cv2.createTrackbar('Gain','CameraSettings',0,127,nothing)
    cv2.createTrackbar('Exposure','CameraSettings',1,12,nothing)
    cv2.createTrackbar('White_balance','CameraSettings',4000,7000,nothing)
    cv2.createTrackbar('Focus','CameraSettings',0,51,nothing)

    cv2.setTrackbarPos('Brightness','CameraSettings', 120)
    cv2.setTrackbarPos('Contrast','CameraSettings', 50)
    cv2.setTrackbarPos('Saturation','CameraSettings', 70)
    cv2.setTrackbarPos('Gain','CameraSettings', 50)
    cv2.setTrackbarPos('Exposure','CameraSettings', 3)
    cv2.setTrackbarPos('White_balance','CameraSettings', 5000)
    cv2.setTrackbarPos('Focus','CameraSettings', 0)

    cap = cv2.VideoCapture(1)

    while 1:
        okay, frame = cap.read()
        cv2.imshow("cap", frame)
        cv2.waitKey(1)

        cap.set(10, cv2.getTrackbarPos('Brightness', 'CameraSettings'))  # brightness     min: 0   , max: 255 , increment:1
        cap.set(11, cv2.getTrackbarPos('Contrast', 'CameraSettings'))  # contrast       min: 0   , max: 255 , increment:1
        cap.set(12, cv2.getTrackbarPos('Saturation', 'CameraSettings'))  # saturation     min: 0   , max: 255 , increment:1
        cap.set(14, cv2.getTrackbarPos('Gain', 'CameraSettings'))  # gain           min: 0   , max: 127 , increment:1
        cap.set(15, -cv2.getTrackbarPos('Exposure', 'CameraSettings'))  # exposure       min: -7  , max: -1  , increment:1
        cap.set(17, cv2.getTrackbarPos('White_balance', 'CameraSettings'))  # white_balance  min: 4000, max: 7000, increment:1
        cap.set(28, cv2.getTrackbarPos('Focus', 'CameraSettings') * 5)  # focus          min: 0   , max: 255 , increment:5