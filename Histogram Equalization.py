# Code 1 : plotting histogram

"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (2).png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0,256])

cv2.imshow('window', img)
plt.plot(hist)
plt.show()

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows() """


# Code 2 : 

""" 
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (2).png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist)

image_hist = cv2.equalizeHist(img_gray) # normal histogram equalization

hist = cv2.calcHist(images=[image_hist], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist) 

cv2.imshow('window', img)
cv2.imshow('img_equalized', image_hist)
plt.show()

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
"""

# Code 2 : (With Comments)

# Global Histogram Equalization :

""" import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (2).png")

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute and plot the histogram of the original grayscale image
hist = cv2.calcHist([img_gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist)

        # histSize -> no. of bins (as the pixel values can range from 0 to 255) therefore, the number of bins is 256

        # all the values have to be passed as lists 

        # channels for a gray scale image is 0 

        # if we pass a mask, the pixels of the image from the mask wouldn't be considered

        # ranges -> range of the bin is 0 to 255, that's why [0,256]

# Apply histogram equalization to the grayscale image
image_hist = cv2.equalizeHist(img_gray)

# Compute and plot the histogram of the equalized grayscale image
equalized_hist = cv2.calcHist([image_hist], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(equalized_hist)

# Display the original and equalized images

cv2.imshow('Image before histogram equalization', img)
cv2.imshow("Gray scale image", img_gray)
cv2.imshow('Image after histogram equalization', image_hist)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()  """


# Code 3 : To get the histogram of a color image

""" 
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (2).png")
b, g, r = cv2.split(img) # splits the color channels of the image

cv2.imshow("Image Window", img)

hist = cv2.calcHist(images=[b], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist)

hist = cv2.calcHist(images=[g], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist)

hist = cv2.calcHist(images=[r], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist)

plt.show() 

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
"""


# Code 4 : Enhancing only the value channel of an image - applying histogram equalization only on the value channel of a color image

""" import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (2).png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(img_hsv)

v = cv2.equalizeHist(v)

merged_hsv = cv2.merge((h,s,v))
 
bgr_enhanced = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("enhanced image", bgr_enhanced)

cv2.imshow("original image", img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows() """


# Code 5 : CLAHE - contrast limited adaptive histogram equalization

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\OMOLP094\\Desktop\\GitHub_Repos_Of_Projects\\Adaptive-Hold-Placement-Algorithm-for-Personalized-Indoor-Climbing-Experiences\\hold_images\\edge.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# normal histogram equalization
normal_hist_img = cv2.equalizeHist(img_gray)

# Contrast limited adaptive histogram equalization (CLAHE)
# declaring CLAHE with the clip limit

clahe = cv2.createCLAHE(clipLimit=5) # clipping limit
clahe_output = clahe.apply(img_gray)

# ordinary thresholding on the same image

_, ordinary_thresh = cv2.threshold(img_gray, 155, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Normal HE Output", normal_hist_img)
cv2.imshow("CLAHE Output", clahe_output)
cv2.imshow("Thresholded Image", ordinary_thresh)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
 