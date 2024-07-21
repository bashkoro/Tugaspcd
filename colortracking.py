import cv2
import numpy as np

# Load the image
image = cv2.imread('bangundatar.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range to track
lower_color = np.array([66, 98, 100])
upper_color = np.array([156, 232, 255])

# Create a mask for the color range
mask = cv2.inRange(hsv, lower_color, upper_color)

# Find the contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw a bounding box around the largest contour
if len(contours) > 0:
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the processed image
cv2.imshow('Color Tracking', image)
cv2.waitKey(0)
cv2.destroyAllWindows()