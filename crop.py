import cv2

# Load the image
image = cv2.imread('1311975.jpg')

# Display the image
cv2.imshow('Original Image', image)

# Define the region of interest (ROI) - change these values to your needs
x, y, w, h = 1000, 100, 500, 500  # x, y are the top-left coordinates; w, h are width and height

# Crop the image
cropped_image = image[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)

# Save the cropped image
cv2.imwrite('path/to/save/cropped_image.jpg', cropped_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
