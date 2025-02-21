# Here are a few examples of different things that can be achieved using perspective transformations in OpenCV:

# Example 1: Rectifying a Document Image

# In this example, we'll correct the perspective of a document image, making it appear as if it was taken straight-on.

""" import cv2
import numpy as np

# Load an image
image = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png')

# Define source and destination points for perspective transformation
source_points = np.float32([[20, 30], [40, 50], [60, 70], [80, 90]])
destination_points = np.float32([[18, 27], [80, 37], [48, 100], [100, 80]])

# Get perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Apply perspective transformation
rectified_image = cv2.warpPerspective(image, perspective_matrix, (100, 200))

# Display the original and rectified images
cv2.imshow('Original Image', image)
cv2.imshow('Rectified Image', rectified_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


# Example 2: Changing Perspective of a Building

# In this example, we'll simulate viewing a building from a different angle, giving it a tilted appearance.

""" import cv2
import numpy as np

# Load an image of a building
image = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png')

# Define source and destination points for perspective transformation
source_points = np.float32([[140, 220], [650, 220], [20, 800], [750, 800]])
destination_points = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])

# Get perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Apply perspective transformation
tilted_image = cv2.warpPerspective(image, perspective_matrix, (400, 600))

# Display the original and tilted images
cv2.imshow('Original Image', image)
cv2.imshow('Tilted Image', tilted_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


# Example 3: Changing the Perspective of an Artwork

# In this example, we'll simulate viewing an artwork from a different angle, creating a skewed effect.

""" import cv2
import numpy as np

# Load an image of an artwork
image = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png')

# Define source and destination points for perspective transformation
source_points = np.float32([[20, 30], [40, 50], [60, 70], [80, 90]])
destination_points = np.float32([[0, 0], [80, 0], [0, 100], [100, 80]])

# Get perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Apply perspective transformation
skewed_image = cv2.warpPerspective(image, perspective_matrix, (300, 400))

# Display the original and skewed images
cv2.imshow('Original Image', image)
cv2.imshow('Skewed Image', skewed_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """

# These examples demonstrate how perspective transformations can be used to achieve different effects, from correcting the view of documents to simulating viewing scenes from various angles. Keep in mind that the accuracy of the transformations depends on the accuracy of the chosen source and destination points.