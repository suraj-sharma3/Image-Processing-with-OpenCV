""" 
Foreground Object: The foreground object is the main subject or the region of interest in an image. It represents the primary content that you are interested in analyzing, manipulating, or segmenting. In a binary image, where there are only two possible pixel values (typically black and white), the foreground is typically represented by the white pixels. For example, if you're analyzing a picture of a person, the person themselves would be the foreground object.

Background Object: The background object is everything that is not part of the main subject or region of interest in the image. It serves as a context for the foreground object. In a binary image, the background is typically represented by the black pixels. Using the example of a person, the area around the person, the surroundings, and any other objects that are not the person would be considered the background.

It's important to note that the distinction between foreground and background is often context-dependent and can vary depending on the specific analysis or processing you're performing on the image. These terms are used to facilitate image segmentation, object detection, and other image processing tasks where isolating the main subject from its surroundings is necessary. """

# Code Examples : 

import cv2
import numpy as np

# Load a binary image (black and white)
image = cv2.imread("C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 4\\images\\opencv.png", cv2.IMREAD_GRAYSCALE)



# Define a kernel
kernel = np.ones((5, 5), np.uint8)

# Erosion: Erosion is a morphological operation that erodes away the boundaries of the foreground object (white region) in a binary image. It works by moving the kernel over the image, and a pixel is considered white (foreground) only if all the pixels under the kernel are white.

# Erosion
erosion = cv2.erode(image, kernel, iterations=1)

""" 
Erosion:
Erosion is like wearing down the edges of an object. Imagine you have a white shape on a black background. When you apply erosion, you move a small square (kernel) over the image. If all the pixels under the kernel are white, the center pixel remains white; otherwise, it turns black. It makes the object smaller and removes small bumps.

Parameters:

image: The image you want to process.
kernel: A small grid that determines the shape of the erosion.
iterations: How many times to apply the erosion. One time is usually enough to make the edges smoother. """

# Dilation: Dilation is the opposite of erosion. It expands the boundaries of the foreground object by adding pixels to the boundary. A pixel is considered white (foreground) if at least one pixel under the kernel is white.

# Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

""" 
Dilation: Dilation is the opposite of erosion. It's like adding some extra space to the edges of an object. When you apply dilation, if at least one pixel under the kernel is white, the center pixel becomes white. It makes the object bigger and fills small gaps.

Parameters:

image: The image you want to process.
kernel: The same small grid as used in erosion.
iterations: How many times to apply dilation. One time is usually enough to make the edges smoother. """

# Opening: Opening is an operation that involves erosion followed by dilation. It's often used to remove noise and small objects while preserving the overall structure of larger objects.

# Opening (erosion followed by dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

""" 
Opening: Opening is a combination of erosion followed by dilation. It's like cleaning up small specks of dirt on a surface. Erosion removes small bits, and then dilation expands what's left.

Parameters:

image: The image you want to process.
kernel: The small grid used for both erosion and dilation.
iterations: The number of times to do erosion and then dilation. """

# Closing: Closing is the reverse of opening – it involves dilation followed by erosion. It's useful for closing small holes and gaps in the foreground while maintaining the overall shape.

# Closing (dilation followed by erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

""" 
Closing: Closing is the opposite of opening. It's like fixing small holes and gaps in an object. Dilation fills gaps, and then erosion smoothens the edges.

Parameters:

image: The image you want to process.
kernel: The small grid used for both dilation and erosion.
iterations: The number of times to do dilation and then erosion. """

# Morphological Gradient: The morphological gradient is the difference between dilation and erosion of an image. It highlights the boundaries of objects in the image.

# Morphological Gradient (difference between dilation and erosion)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

""" 
Morphological Gradient:
The gradient shows the difference between dilation and erosion. It highlights the edges of objects.

Parameters:

image: The image you want to process.
kernel: The small grid used for both dilation and erosion. """

""" 
Morphological Gradient:
The Morphological Gradient is a morphological operation that helps us understand the abrupt changes or edges in an image. It's like outlining the parts of an object that have strong changes in intensity. This is particularly useful for detecting the boundaries of objects in an image.

Imagine you have a black-and-white image, where the white parts are the objects of interest and the black parts are the background. The Morphological Gradient shows us where these objects change rapidly from white to black or vice versa. """

""" Here's how it works:

Dilation:
Start by dilating the original image. Dilation expands the white areas. Now, compare this dilated image to the original. The white areas in the dilated image have now expanded into the neighboring areas.

Erosion:
Next, erode the original image. Erosion shrinks the white areas. Again, compare the eroded image to the original. The white areas in the eroded image have now shrunk, leaving the original white areas untouched.

Difference:
Subtract the eroded image from the dilated image. This highlights the difference between the two, which corresponds to the edges or rapid intensity changes in the original image.

In simpler terms, the Morphological Gradient gives you a picture that shows where the image changes from dark to light or light to dark quickly. This is useful when you want to detect where different objects meet or where there's a transition between the foreground and background. """
cv2.imshow("Original", image)

cv2.imshow("Transformed", erosion)
k = cv2.waitKey(0) 
if k == ord('q'):
    cv2.destroyAllWindows()

# Finally, the code displays the original and morphologically transformed images using cv2.imshow(). The cv2.waitKey(0) waits for a key press, and then cv2.destroyAllWindows() closes all the displayed windows.

# Remember to replace 'binary_image.png' with the actual path to your binary image file.