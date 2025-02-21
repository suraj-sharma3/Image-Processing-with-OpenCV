""" # Scaling: Scaling refers to resizing an image to make it larger or smaller. It's useful for adjusting the image size while maintaining its aspect ratio.

import cv2

# Load an image
image = cv2.imread('image.jpg')

# Define the scaling factor
scaling_factor = 0.5

# Apply scaling
scaled_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)

# Display the original and scaled images
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Translation: Translation shifts an image's position in a certain direction (x and y).

import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Define translation matrix
translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # Shift by (50, 30)

# Apply translation
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Display the original and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Rotation: Rotation changes the orientation of an image by a certain angle.

import cv2

# Load an image
image = cv2.imread('image.jpg')

# Define rotation angle (in degrees)
angle = 45

# Get rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)

# Apply rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


# Perspective Transformation: Perspective transformation allows you to change the perspective of an image as if it's viewed from a different angle.

""" While perspective transformation and zooming in/out of an image can sometimes appear similar, they are not quite the same thing.

Perspective transformation involves changing the perspective of an image to simulate viewing it from a different angle or position. This transformation can also alter the shape of objects within the image. For example, you can use perspective transformation to correct the distortion caused by photographing a rectangular object at an angle, making it appear as if it's viewed straight-on.

Zooming in/out, on the other hand, typically involves changing the scale of an image to make it appear larger or smaller. This doesn't necessarily change the perspective of the image; it simply magnifies or reduces the contents uniformly. Zooming can be achieved through scaling operations, as we discussed earlier, but it doesn't inherently involve altering the perspective of the objects within the image.

In summary, perspective transformation and zooming both involve manipulating an image, but they have different effects: perspective transformation changes the perspective of objects, while zooming changes the overall size of the image's contents. """

import cv2
import numpy as np

# Load an image
image = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png')

# Define source and destination points for perspective transformation
source_points = np.float32([[0, 0], [image.shape[1], 0], [0, image.shape[0]], [image.shape[1], image.shape[0]]])
destination_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])

# Get perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Apply perspective transformation
perspective_transformed_image = cv2.warpPerspective(image, perspective_matrix, (300, 400))

# Display the original and perspective transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Averaging: Averaging is a basic form of image blurring or smoothing. It replaces each pixel's value with the average of its neighboring pixels.

import cv2

# Load an image
image = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png')

# Apply averaging blur
blurred_image = cv2.blur(image, (5, 5))  # Averaging kernel size: 5x5

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Gaussian Blurring: Gaussian blur is a type of blur that uses a Gaussian kernel to apply weighted averaging to pixels, giving a smoother effect.

import cv2

# Load an image
image = cv2.imread('image.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # Gaussian kernel size: 5x5

# image: This is the input image that you want to apply the Gaussian blur to. It should be a 2D or 3D (color) NumPy array representing the image.

# (5, 5): This tuple specifies the size of the Gaussian kernel. The kernel is a matrix that determines the weights used for the averaging process. In this case, the kernel size is set to (5, 5), meaning a 5x5 matrix will be used. The larger the kernel, the more significant the blurring effect. The kernel size should typically be an odd number to ensure a well-defined center for the kernel.

# 0: The third parameter is the standard deviation (sigma) of the Gaussian distribution in the x-direction. A standard deviation of 0 means that OpenCV will calculate it based on the kernel size. If you provide a value for this parameter, OpenCV will use it as the sigma. The larger the sigma, the more the blur. If sigma is set to 0, OpenCV calculates an appropriate value based on the kernel size.
    
# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Median Filtering: Median filtering replaces each pixel's value with the median of its neighboring pixels, which is effective in removing noise.

import cv2

# Load an image
image = cv2.imread('image.jpg')

# Apply median filtering
median_filtered_image = cv2.medianBlur(image, 5)  # Kernel size: 5x5

""" image: This is the input image on which you want to apply the median filtering. It should be a grayscale image (2D array) without any channels, as the median filter is typically applied to single-channel images.

5: This parameter specifies the size of the median filter kernel. The median filter works by replacing each pixel's value with the median value of its neighboring pixels within the specified kernel size. In this case, the kernel size is set to 5, which means a 5x5 neighborhood around each pixel will be considered. Like Gaussian blurring, the kernel size should typically be an odd number to have a well-defined center for the kernel.

The cv2.medianBlur() function calculates the median value of the pixel values in the specified neighborhood (kernel) and replaces the center pixel's value with that median value. This has the effect of reducing noise in the image while preserving edges and finer details. """

# Display the original and median filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


""" 
Gaussian blur and median filtering are both image smoothing techniques used to reduce noise and details in an image, but they work differently and have distinct characteristics.

Gaussian Blur:

How it works: Gaussian blur applies a weighted average to pixels within a certain neighborhood defined by a Gaussian distribution. The weights decrease as pixels move away from the center of the kernel.

Effect on Image: Gaussian blur has a smoothing effect that reduces high-frequency noise and sharp edges. It's effective for removing small-scale noise and creating a continuous gradient effect.

Preservation of Edges: While Gaussian blur does smooth out noise, it also softens edges and details in the image. Edges become less distinct due to the averaging of pixel values.

Kernel Shape: Gaussian blur uses a Gaussian-shaped kernel where weights decrease radially from the center.

Median Filtering:

How it works: Median filtering replaces the value of a pixel with the median value of the pixels within a neighborhood defined by the filter size. The median is the middle value when all pixel values are sorted in ascending order.

Effect on Image: Median filtering is particularly effective at removing salt-and-pepper noise (random isolated bright or dark pixels) while preserving edges and details. It works well when noise is caused by sporadic, isolated anomalies.

Salt and pepper noise, also known as impulse noise, is a type of irregular noise commonly found in images. It manifests as randomly occurring bright and dark pixels that stand out from the surrounding image. These bright pixels resemble grains of salt, while the dark pixels resemble grains of black pepper, hence the name "salt and pepper noise."

Preservation of Edges: Median filtering is better at preserving edges than Gaussian blur. Since the median is not sensitive to extreme values (outliers), edges remain relatively unchanged.

Kernel Shape: Median filtering uses a square or rectangular kernel where pixel values within the neighborhood are sorted and the median is taken.

Summary:

Gaussian blur is generally used to achieve a more subtle overall smoothing effect and is suitable for noise reduction and reducing fine-scale details. It's less effective at preserving edges.

Median filtering is especially useful for removing salt-and-pepper noise and preserving edges. It's a good choice when you want to maintain sharpness in the image while reducing noise.
 """

# Morphological Transformations: Morphological transformations involve operations like erosion, dilation, opening, closing, and morphological gradient. These operations are used for shape manipulation and noise reduction in images.

import cv2
import numpy as np

# Load a binary image (black and white)
image = cv2.imread('binary_image.png', cv2.IMREAD_GRAYSCALE)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# Opening (erosion followed by dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing (dilation followed by erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient (difference between dilation and erosion)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Display the original and morphologically transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()