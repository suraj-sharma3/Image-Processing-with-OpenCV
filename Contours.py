# Contours: Contours are the curves that form the boundaries of objects in an image. They are a fundamental concept in image processing and computer vision, used for tasks like object detection, shape analysis, and more. In simple terms, you can think of contours as the outlines of objects in a picture.

""" 
cv2.findContours:
This function in OpenCV is used to find contours in a binary image. It takes the binary image as input and returns a list of contours. Each contour is represented as a list of points that form the boundary of an object.

contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

Parameters:

binary_image: The binary image in which you want to find contours.
cv2.RETR_EXTERNAL: Specifies the retrieval mode. EXTERNAL retrieves only the outermost contours.
cv2.CHAIN_APPROX_SIMPLE: Specifies the contour approximation method, which simplifies the contour while retaining its basic shape. """


# drawContours: Once you have found contours, you can draw them on an image using the drawContours function. This function helps visualize the contours on an image.

""" 
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
Parameters:

image: The image on which you want to draw the contours.
contours: The list of contours you obtained from cv2.findContours.
-1: This specifies that you want to draw all contours.
(0, 255, 0): The color of the contours (in BGR format).
2: The thickness of the contour lines.


Contour Approximation Method:
Contours can have many points, making them complex. The contour approximation method simplifies the contour while retaining its shape. This can be useful when you want to reduce the number of points for efficiency. """


# Contour Area and Perimeter:

""" Contour Area: This is the area enclosed by a contour. You can use cv2.contourArea(contour) to calculate it.

Contour Perimeter: This is the length of the contour's boundary. You can use cv2.arcLength(contour, closed=True) to calculate it.

Bounding Rectangle:
A bounding rectangle is the smallest rectangle that can enclose a contour. It's helpful for creating a simple box around an object.


x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
Here, (x, y) are the top-left coordinates of the rectangle, and (w, h) are its width and height. """

# In summary, contours are essential tools in image processing for object detection and analysis. cv2.findContours helps you find them, drawContours helps you visualize them, the contour approximation method simplifies them, and functions like contourArea, arcLength, and boundingRect provide information about their properties.


# Finding Contours and Drawing Them:


import cv2
import numpy as np

# Load an image
image = cv2.imread('contour_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)

# Find contours
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the image with contours
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()




""" # 2. Contour Approximation:


import cv2
import numpy as np

image = cv2.imread('contour_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

cv2.imshow('Contour Approximation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Contour Area and Perimeter:


import cv2
import numpy as np

image = cv2.imread('contour_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    print(f"Contour Area: {area}, Contour Perimeter: {perimeter}")

cv2.imshow('Contour Area and Perimeter', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Bounding Rectangle:

import cv2
import numpy as np

image = cv2.imread('contour_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Bounding Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows() """