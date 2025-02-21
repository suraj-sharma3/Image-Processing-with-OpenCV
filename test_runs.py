import cv2

# Load an image
image = cv2.imread("C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 5\\images\\omotec.png")

# Apply median filtering
median_filtered_image = cv2.medianBlur(image, 3)  # Kernel size: 5x5

""" image: This is the input image on which you want to apply the median filtering. It should be a grayscale image (2D array) without any channels, as the median filter is typically applied to single-channel images.

5: This parameter specifies the size of the median filter kernel. The median filter works by replacing each pixel's value with the median value of its neighboring pixels within the specified kernel size. In this case, the kernel size is set to 5, which means a 5x5 neighborhood around each pixel will be considered. Like Gaussian blurring, the kernel size should typically be an odd number to have a well-defined center for the kernel.

The cv2.medianBlur() function calculates the median value of the pixel values in the specified neighborhood (kernel) and replaces the center pixel's value with that median value. This has the effect of reducing noise in the image while preserving edges and finer details. """

# Display the original and median filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()