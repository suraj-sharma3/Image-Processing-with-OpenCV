# Edge Detection : High Pass Filtering Operation, The process involves detecting sharp edges in the image & producing a binary image as an output, we draw white lines on a black background to indicate those edges

# Sharp Edge is the edge where intensity of the pixel is changing rapidly & not the colors

# Edge detection is a fundamental technique in computer vision and image processing used to identify and locate boundaries within an image. It aims to highlight areas where there is a rapid change in intensity or color, which often corresponds to the edges or boundaries of objects or features in the image. OpenCV provides several methods for performing edge detection.

""" 
# Sobel Edge Detection:

Explanation: Sobel edge detection is like simulating the process of running your fingers along an image to feel for sudden changes in intensity. It uses two small 3x3 filters (kernels), one for detecting changes in brightness horizontally and the other vertically. These filters emphasize the rate of change of intensity at each pixel.

Effect: It highlights edges by identifying areas where the intensity of an image changes rapidly, both horizontally and vertically.

Application: Sobel edge detection is used for tasks like detecting the edges of objects in images and finding the direction of edges.

______________________________________________________________________________________

# Scharr Edge Detection:

Explanation: Scharr is an improvement over Sobel and is like using more sensitive fingers to feel for edges. It also uses 3x3 filters but with optimized coefficients that provide better rotational symmetry. This means it's better at detecting edges at different angles.

Effect: Scharr is more effective than Sobel in detecting edges that are not aligned with the horizontal or vertical directions.

Application: It's used in edge detection when you need more accurate results, especially for edges at various orientations.

______________________________________________________________________________________


# Laplacian Edge Detection:

Explanation: Laplacian edge detection is like examining how the brightness changes in the entire neighborhood of each pixel. It applies a Gaussian smoothing filter to reduce noise, followed by computing the Laplacian (second derivative) of the smoothed image. The zero-crossings of the Laplacian indicate edges.

Effect: It detects edges by looking for sign changes in the second derivative, making it more robust to noise.

Application: Laplacian edge detection is used when you want accurate edge localization and are less concerned about the edge direction.

______________________________________________________________________________________


# Canny Edge Detection:

Explanation: Canny edge detection is like a multi-step process. It first smoothes the image to reduce noise, then calculates the gradient to find areas with the strongest intensity changes. Non-maximum suppression is applied to thin the edges, and finally, edges are tracked by hysteresis to link adjacent edge points.

Effect: Canny provides precise edge localization and is good at handling noise. It often results in thin, continuous edges.

Application: Canny is widely used in image processing, computer vision, and object detection due to its robustness and accuracy.

______________________________________________________________________________________


# Prewitt Edge Detection:

Explanation: Prewitt edge detection is like using special glasses to focus on changes in brightness. It employs a pair of 3x3 convolution kernels, one for detecting changes in intensity along the horizontal axis and the other along the vertical axis. These kernels emphasize the rate of change of intensity in the image.

Effect: Prewitt identifies edges by highlighting areas where the intensity changes quickly, both horizontally and vertically. It emphasizes both horizontal and vertical edges separately.

Application: Prewitt edge detection is used for tasks such as finding edges in images, edge enhancement, and gradient-based feature extraction. It's particularly effective when you want to emphasize edges in specific directions while keeping them distinct from other edges in the image. 

______________________________________________________________________________________
"""

# Canny Edge Detection : 

# Five Steps of Canny Edge Detection : 

""" 
1) Noise Reduction:

# In OpenCV, "noise" refers to random and unwanted variations in the colors or brightness of pixels in an image. Imagine you take a photo with your camera, but the picture doesn't turn out perfectly smooth. Instead, it has little specks of random color or brightness scattered around. Those specks are the "noise" in the image.

Explanation: The first step in Canny edge detection is to reduce noise in the image. Noise can be caused by imperfections in the image acquisition process or other factors. To reduce noise, Canny applies a Gaussian smoothing filter to the image. The Gaussian filter blurs the image slightly, which helps in removing high-frequency noise while preserving the edges.

Effect: Noise reduction makes the image cleaner and helps prevent false edge detection caused by noise.

2) Gradient Calculation:

# Gradient is always perpendicular to the Edge direction

Explanation: After noise reduction, Canny calculates the gradient of the image. This involves finding the rate of change of intensity at each pixel. Typically, Canny uses Sobel or Scharr operators to compute the gradient in both the horizontal and vertical directions. The gradient magnitude and direction are computed for each pixel.

Effect: The gradient information highlights areas where intensity changes rapidly, which is a characteristic of edges in the image.

3) Non-Maximum Suppression:

Explanation: To thin the edges and keep only the most significant points, Canny applies non-maximum suppression. For each pixel, it compares the gradient magnitude with its neighbors in the direction of the gradient. If the pixel has the maximum gradient magnitude among its neighbors, it is considered an edge point; otherwise, it is suppressed (set to zero).

Effect: Non-maximum suppression ensures that only the strongest edges are retained, reducing the thickness of the detected edges.

4) Double Thresholding:

Explanation: In this step, Canny uses two threshold values: a high threshold (T_high) and a low threshold (T_low). Pixels with gradient magnitudes above T_high are considered strong edge candidates, and pixels with gradient magnitudes below T_low are discarded. Pixels with gradient magnitudes between T_low and T_high are considered weak edge candidates.

Effect: Double thresholding helps classify edge pixels into strong and weak categories, allowing for better edge tracking in the next step.

5) Edge Tracking By Hysteresis:

Explanation: To link and finalize edges, Canny performs edge tracking by hysteresis. It starts from the strong edge pixels identified in the previous step and follows the weak edge pixels that are connected to strong edges. If a weak pixel is connected to a strong pixel, it is considered part of the edge; otherwise, it is discarded.

Effect: Edge tracking ensures that edges are continuous and connected, even in the presence of noise or gaps in the edge information. """


#import the dependencies
import cv2
import numpy as np


image = cv2.imread('C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\Image (1).png', 0)
# image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# resizing the image
image = cv2.resize(image, None, fx=0.5,fy=0.3)

# performing the edge detetcion
gradients_sobelx = cv2.Sobel(image, -1, 1, 0) # for sobelx, dx = 1 & dy = 0

""" 
gradients_sobelx = cv2.Sobel(image, -1, 1, 0) computes the horizontal gradient of the image (sobelx). It's done using the Sobel operator, which highlights the rate of change of intensity from left to right in the image. The parameters used are:

image: The input image on which the gradient operation is applied.
-1: The data type of the output image. Here, it's set to -1, which means it will use the same data type as the input image.
1 and 0: These values represent the direction of the gradient. 1 for dx means that the gradient is calculated in the horizontal (x) direction (left to right), and 0 for dy means that no gradient is calculated in the vertical (y) direction. This computes the horizontal gradient component. """

gradients_sobely = cv2.Sobel(image, -1, 0, 1) # for sobelx, dx = 0 & dy = 1

""" 
gradients_sobely = cv2.Sobel(image, -1, 0, 1) computes the vertical gradient of the image (sobely). It uses the Sobel operator to highlight the rate of change of intensity from top to bottom in the image. The parameters used are:

image: The input image on which the gradient operation is applied.
-1: The data type of the output image, which is set to -1 to use the same data type as the input image.
0 and 1: These values represent the direction of the gradient. 0 for dx means that no gradient is calculated in the horizontal (x) direction, and 1 for dy means that the gradient is calculated in the vertical (y) direction (top to bottom). This computes the vertical gradient component. """
    
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

# dst = alpha * src1 + beta * src2 + gamma
# alpha: This is the weight applied to the first image (src1).
# beta: This is the weight applied to the second image (src2).
# gamma: This is an optional scalar value added to the final result.

# The gamma parameter serves as an offset or bias, allowing you to control the overall brightness or darkness of the resulting image. By adjusting the gamma value, you can shift the brightness level of the output image.

# Here's how it works:

## If gamma is set to a positive value, it will add that value to every pixel in the final result. This effectively brightens the entire image by the specified amount.

## If gamma is set to a negative value, it will subtract that value from every pixel in the final result. This darkens the entire image by the specified amount.

## When gamma is set to 0, it has no effect on the brightness of the final result. The image remains unchanged in terms of brightness due to the gamma parameter.

gradients_laplacian = cv2.Laplacian(image, -1)

# cv2.Laplacian Function:

## image: This is the input image on which the Laplacian operation is applied.
## -1: The data type of the output image. When set to -1, it means that the output image will use the same data type as the input image.

## Effect: The Laplacian operator is used to highlight regions where the intensity changes quickly, such as edges or corners, in the image. It does this by calculating the sum of second-order derivatives in both the horizontal and vertical directions.

## Positive values in the Laplacian result represent areas where the intensity increases rapidly (edges), while negative values represent areas where the intensity decreases rapidly (edges with darker regions).

canny_output = cv2.Canny(image, 80, 150)

# 80 & 150 will be used for non-max suppression all the edge pixels with a value less than 80 will be removed & all the edge pixels with a value more than 150 will be considered during non-max suppression & hysteresis would take care of all the edge pixels with a value in between 80 & 150

cv2.imshow('Sobel x', gradients_sobelx)
cv2.imshow('Sobel y', gradients_sobely)
cv2.imshow('Sobel X+y', gradients_sobelxy)
cv2.imshow('laplacian', gradients_laplacian)
cv2.imshow('Canny', canny_output)
cv2.waitKey()































""" 
Edge detection is a fundamental technique in computer vision and image processing used to identify and locate boundaries within an image. It aims to highlight areas where there is a rapid change in intensity or color, which often corresponds to the edges or boundaries of objects or features in the image. OpenCV provides several methods for performing edge detection. Here's an overview of edge detection in OpenCV:

# Gradient-Based Methods:

## Sobel Operator: The Sobel operator is used to compute the gradient of an image by applying convolution with a pair of 3x3 kernels (one for detecting changes in the horizontal direction and the other for the vertical direction). The magnitude of the gradient at each pixel represents the strength of the edge, and its direction indicates the orientation of the edge.

## Scharr Operator: Similar to the Sobel operator, the Scharr operator is used to compute gradient information but is designed to provide better rotational symmetry and improved performance for edge detection.

## Prewitt Operator: Similar to the Sobel operator, the Prewitt operator is another method for computing the gradient of an image and is often used for edge detection.

# Canny Edge Detector:

The Canny edge detector is a widely used method for edge detection in OpenCV. It combines multiple steps, including Gaussian smoothing, gradient computation, non-maximum suppression, and edge tracking by hysteresis. The Canny detector is effective at detecting edges while suppressing noise and providing accurate localization of edges.
Laplacian of Gaussian (LoG):

The LoG edge detection method involves applying a Gaussian smoothing filter to the image to reduce noise and then computing the Laplacian (second derivative) of the smoothed image. The zero-crossings of the Laplacian indicate the locations of edges. It is less susceptible to noise compared to simple gradient-based methods.
Zero Crossing Edge Detector:

This method identifies edges by detecting zero-crossings in the gradient magnitude of the image. It's a straightforward technique but can be sensitive to noise.
Corners and Junctions Detection:

In addition to detecting edges, OpenCV provides methods to detect corners and junctions in an image. The Harris corner detector and Shi-Tomasi corner detector are examples of techniques used to locate key points (corners) in an image.
Custom Edge Detection Filters:

You can also create custom edge detection filters by designing convolution kernels that highlight specific types of edges or features in an image. Custom filters can be useful for specialized edge detection tasks. """