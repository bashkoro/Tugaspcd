import cv2
import numpy as np

def nothing(x):
    pass

# Load the image
image = cv2.imread('1315490.jpg')

cv2.namedWindow('Trackbars')
cv2.createTrackbar('L-H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('L-S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L-V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-H', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('U-S', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('U-V', 'Trackbars', 255, 255, nothing)

while True:
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('L-H', 'Trackbars')
    l_s = cv2.getTrackbarPos('L-S', 'Trackbars')
    l_v = cv2.getTrackbarPos('L-V', 'Trackbars')

    u_h = cv2.getTrackbarPos('U-H', 'Trackbars')
    u_s = cv2.getTrackbarPos('U-S', 'Trackbars')
    u_v = cv2.getTrackbarPos('U-V', 'Trackbars')

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('frame', image)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()