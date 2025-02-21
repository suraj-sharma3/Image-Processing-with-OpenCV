# Contour Retrieval Mode : decides how the retrieved contours have to be stored, there can be several contours in an image, there could be inner contours, outer contours, etc. contour retrieval mode decides how & which of these detected contours have to be stored

# 1) Retrieve external (cv2.RETR_EXTERNA): outputs only the external contours, e.g. if we have concentric circles, the contours of the outer circle will be stored, contours of the inner circle will be ignored

# 2) Retrieve List (cv2.RETR_LIST): outputs all the contours without any hierarchical relationship (all the contours of the image would be stored, but there would be no hierarchy (there wouldn't be any parent or child contours)), hierarchy variable used with findContours methods stores the information about the hierarchy of the contours detected in an image

# 3) Retrieve Tree (cv2.RETR_TREE): outputs all the contours by establishing a hierarchical relationship among the contours, there would be hierarchy (there would be parent & child contours))


""" 
In OpenCV, the contour retrieval mode is a parameter used in the findContours function to determine how contours should be retrieved from a binary image. The choice of retrieval mode affects which contours are detected and how they are organized. OpenCV provides several retrieval modes, and the choice depends on your specific requirements for contour analysis. Here are some common contour retrieval modes:

# cv2.RETR_EXTERNAL: This mode retrieves only the external (outermost) contours. It ignores all contours that are contained within others. This is useful when you want to identify and work with the contours of individual objects in an image.

# cv2.RETR_LIST: This mode retrieves all the contours without establishing any hierarchical relationships between them. It is simple and efficient but does not provide information about nested contours.

# cv2.RETR_CCOMP: This mode retrieves all the contours and organizes them into a two-level hierarchy. Contours that belong to the same external contour are at the top level, and contours that are internal holes or boundaries are at the second level. This mode is useful for detecting objects and their internal structures.

# cv2.RETR_TREE: This mode retrieves all the contours and reconstructs a full hierarchy of nested contours. It provides the most detailed information about the relationships between contours, including parent-child relationships. It is useful when you need to understand the hierarchical structure of objects in an image. """


"""
Explanation of Hierarchy obtained by using cv2.RETR_TREE retrieval mode : 

# When you use the cv2.RETR_TREE retrieval mode with the findContours function in OpenCV, the hierarchy of contours is stored in the hierarchy variable. The hierarchy information represents the relationships between different contours, including parent-child relationships. The hierarchy variable is typically a NumPy array that allows you to navigate and understand the structure of the detected contours.

The hierarchy information is organized as a 4-channel array, where each row corresponds to a contour in the contours list returned by findContours. The four values stored in each row represent the following information for the corresponding contour:

# The index of the next contour on the same hierarchical level.
# The index of the previous contour on the same hierarchical level.
# The index of the first child contour (internal hole) if any.
# The index of the parent contour (the external contour that encloses the current contour).

Here is an example to illustrate how the hierarchy information is structured. Let's say you have the following contours detected in an image:

# Contour 0: The largest external contour.
# Contour 1: A child contour contained within Contour 0.
# Contour 2: Another external contour at the same level as Contour 0.
# Contour 3: An internal contour (hole) within Contour 2.

The hierarchy information might look like this:

hierarchy = [
    # next, prev, first child, parent
    [-1, -1,  1, -1],  # Contour 0
    [-1,  0, -1, -1],  # Contour 1 (child of Contour 0)
    [-1, -1,  3, -1],  # Contour 2
    [-1, -1, -1,  2]   # Contour 3 (child of Contour 2)
]

# For Contour 0, the next contour at the same level is -1 (none), the previous contour is -1 (none), it has one child (Contour 1), and it has no parent (external contour).

# For Contour 1, the next contour is -1 (none), the previous contour is 0, it has no children, and its parent is Contour 0.

# For Contour 2, the next contour at the same level is -1 (none), the previous contour is -1 (none), it has one child (Contour 3), and it has no parent (external contour).

# For Contour 3, the next contour is -1 (none), the previous contour is -1 (none), it has no children, and its parent is Contour 2.

# This hierarchy information allows you to navigate the relationship between contours and determine which contours are external, which are internal, and how they are nested within each other. It's particularly useful when you want to perform advanced contour analysis or when you need to separate objects with holes from the external objects. """


import cv2
import numpy

#Read the image and convert it to grayscale
image = cv2.imread('C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Geometric-solids.jpg')
image = cv2.resize(image, None, fx=0.4,fy=0.4)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Now convert the grayscale image to binary image
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Now detect the contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_TC89_KCOS)

#Visualize the data structure
print("Length of contours {}".format(len(contours)))
# print(contours)

print("Hierarchy of detected contours : ")
print(hierarchy)


# draw contours on the original image
image_copy = image.copy()
image_copy = cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

#Visualizing the results
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Drawn Contours', image_copy)
cv2.imshow('Binary Image', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()