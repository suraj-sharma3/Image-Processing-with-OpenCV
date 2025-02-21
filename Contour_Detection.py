# Contour : boundary around something that has well defined edges, so that the machine can calculate the difference in gradient & form a recognisable shape through continuous tracking of change in pixel intensities & drawing as boundary around it

# Gradient - Random / Sudden changes in the intensities of the pixel values in an image

# By continuous tracking of gradient in the image, the edges of the objects are captured which are nothing but contours

# through contour detection, we can detect the outlines (borders) of objects. 
# Uses : Object detection or recognition

# contour detection can only be performed over binary images (images only containing black (0) & white (255) pixels) as contour detection algorithm tracks the edges (gradients) & gradients can be easily detected in binary images & not in gray scale images

# Functions used : 
'''
1) findContours() : 

Parameters :-

    # image - binary image
    # mode - contour retrieval mode
    # method - contour approximation method

'''

'''
2) drawContours() : Contours are a way to represent the boundaries of objects in an image, and the drawContours function allows you to visualize these contours by drawing them on an image.

Parameters :-

    # image - original input BGR image
    # contours - contours obtained using findContours() function, contours obtained are stored within a list

    # contour index - This parameter specifies the index of the contour you want to draw. You can pass -1 to draw all the contours in the contours list. If you want to draw a specific contour, you can provide its index in the list. For example, if you have multiple contours and you want to draw the first one, you would pass 0 as the contourIdx.

    # contour index = -1 will draw all the detected contours

    # color - color of the contours you want to draw
    # thickness - The thickness of the contour lines. If you set it to a negative value (e.g., -1), the contour will be filled.

'''


import cv2
# import numpy

#Read the image and convert it to grayscale
image = cv2.imread("C:\\Users\\OMOLP094\\Downloads\\cracked_pipe_cropped.jpg")

print(image.shape)

# resizing the image
image = cv2.resize(image, None, fx=3, fy=3)

# for thresholding, we need a gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Now convert the grayscale image to binary image
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
# gray: This is the input grayscale image on which you want to perform thresholding.

# 0: This is the threshold value. In this case, it's set to 0. The threshold value is used to separate pixels into two categories: those below the threshold and those equal to or above it.

# 255: This is the maximum value that will be assigned to pixels that meet the threshold condition. In binary thresholding, pixels that meet the condition are set to this maximum value (white), and those that don't are set to 0 (black).

# cv2.THRESH_BINARY + cv2.THRESH_OTSU: These are thresholding flags. In this line of code, both binary thresholding and Otsu's thresholding are used simultaneously.

# cv2.THRESH_BINARY: This flag specifies binary thresholding, where pixels with intensity values greater than or equal to the threshold value are set to the maximum value (255), and pixels below the threshold are set to 0.

# cv2.THRESH_OTSU: This flag specifies Otsu's thresholding method. Otsu's method automatically calculates an optimal threshold value by minimizing the intraclass variance of the two classes of pixels (foreground and background). It's useful when you don't know the appropriate threshold value to use.

# ret: This variable holds the threshold value that Otsu's method calculated. It can be useful if you want to know the threshold value determined by Otsu's method.

# binary: This is the thresholded binary image where pixels that meet the threshold condition are set to 255 (white), and pixels that don't meet the condition are set to 0 (black).
'''

#Now detect the contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# [128, 156, 233]

'''
# binary: This is the input binary image in which you want to find contours. A binary image typically consists of only two pixel values, often representing objects of interest (e.g., foreground) and the background. Contours are sought within this binary image.

# mode=cv2.RETR_TREE: The mode parameter specifies the retrieval mode for the contours. In this case, you've set it to cv2.RETR_TREE. This mode retrieves all the contours and reconstructs a full hierarchy of nested contours, including external and internal contours. The hierarchy information can be useful when you want to understand the relationships between different contours.

# method=cv2.CHAIN_APPROX_NONE: The method parameter specifies the contour approximation method. You've set it to cv2.CHAIN_APPROX_NONE, which means that no approximation is applied to the contours, and they are stored with all their points. This is useful when you need the precise shape of the contours. If memory or processing efficiency is a concern, you can use other approximation methods, such as cv2.CHAIN_APPROX_SIMPLE, which approximates contours with fewer points while preserving their overall shape.

# After running this line of code, you'll have two variables:

# contours: This variable will contain a list of all the contours found in the binary image. Each contour is represented as a list of points.

# hierarchy: This variable will contain information about the hierarchy of contours, especially useful when contours are nested within one another. The hierarchy is represented as a nested Python list, and it can be used to identify parent-child relationships between contours.
'''

#Visualize the data structure - printing the length of the list that contains the contours & the list itself
print("Length of contours {}".format(len(contours)))
# print(contours)
print(hierarchy)

# draw contours on the original image
image_copy = image.copy()
image_copy = cv2.drawContours(image_copy, contours[11:20], -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# even if we remove "lineType=cv2.LINE_AA", the code would still work
# lineType=cv2.LINE_AA: This parameter sets the line type used for drawing the contours. cv2.LINE_AA represents anti-aliased (smooth) lines, which can provide smoother and more visually appealing contour edges.

""" 
Here are some of the commonly used line types:

# cv2.LINE_4: This represents a 4-connected line. It is the default line type and is suitable for most cases.

# cv2.LINE_8: This represents an 8-connected line, allowing for diagonally connected pixels as well. It provides more connectivity compared to cv2.LINE_4.

# cv2.LINE_AA (Anti-aliased): This represents anti-aliased lines, which provide smoother and visually better results compared to the regular line types. It's often used for drawing high-quality lines. """


cv2.imshow("image window", image)
# #Visualizing the results
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Drawn Contours', image_copy)
cv2.imshow('Binary Image', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()