""" Perspective transformation, also known as homography transformation, is a geometric transformation that is commonly used in computer vision and image processing. It is used to manipulate the perspective view of an image, allowing you to change the apparent positions of points in a way that simulates the effects of a three-dimensional perspective.

In simple terms, perspective transformation can be used to correct or simulate the distortion that occurs when viewing a three-dimensional scene from a specific angle. It's particularly useful when dealing with images of objects or scenes taken from different viewpoints, or when trying to extract specific regions of interest from images.

Perspective transformation involves mapping the points in an image to new positions based on a transformation matrix. This matrix is determined by corresponding points in the original image and their corresponding desired positions in the transformed image. These corresponding points define the source and destination points for the transformation.

The transformation matrix is used to perform various operations, including rotation, scaling, translation, and skewing, which collectively simulate the effects of changing the perspective of the scene """

""" import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 3\\images\\sudoku.png')

# Get dimensions of the input image (height, width, channels)
rows, cols, ch = img.shape

# Define source and destination points for perspective transformation
# These points help define how the transformation will be applied
pts1 = np.float32([[56, 65], [500, 52], [28, 500], [500, 500]])  # Source points in the input image
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])    # Corresponding destination points in the output image

pts3 = np.float32([[40, 70], [17, 63], [89, 70], [300, 200]])  # Source points in the input image
pts4 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])    # Corresponding 

# Calculate the perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation to the image
# The warpPerspective function applies the transformation defined by the matrix 'M'
# to the input image, resulting in the 'dst' (destination) image
dst = cv2.warpPerspective(img, M, (300, 300))  # Output image size: 300x300

# Create a matplotlib figure with subplots
plt.subplot(121)  # First subplot: original input image

The value 121 is used to specify the position of the subplot within a grid of subplots in a matplotlib figure. The syntax for subplot() is subplot(nrows, ncols, index).

nrows: This parameter specifies the number of rows in the grid of subplots.
ncols: This parameter specifies the number of columns in the grid of subplots.
index: This parameter specifies the position of the subplot within the grid.
In the case of plt.subplot(121), you are creating a grid of subplots with 1 row and 2 columns. This means you have a single row that can accommodate two subplots side by side. Now, let's interpret the value 121:

The first digit, 1, represents the number of rows in the grid. Since you have specified 1 here, you will have a single row in your grid.

The second and third digits, 21, represent the position of the subplot within the grid. The first digit 2 indicates that there are two columns in the grid. The next two digits, 1, indicate that the subplot you're creating will be the first one in the first row.

So, when you use plt.subplot(121), you're specifying that you want to create the first subplot in a grid that has 1 row and 2 columns. In other words, you're creating the first subplot at the top-left position of the grid. 

plt.imshow(img)
plt.title('Input')  # Title for the first subplot

plt.subplot(122)  # Second subplot: transformed output image
plt.imshow(dst)
plt.title('Output')  # Title for the second subplot

# Display the matplotlib figure with both subplots
plt.show()  # Display the figure containing both input and output images
# Don't forget to close the parentheses here """


""" import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 3\\images\\sudoku.png')

# Define source and destination points for perspective transformations
pts1 = np.float32([[56, 65], [500, 52], [28, 500], [500, 500]])
pts2_list = [
    np.float32([[0, 0], [300, 0], [0, 300], [300, 300]]),  # Destination for output 1
    np.float32([[0, 0], [200, 0], [0, 200], [200, 200]]),  # Destination for output 2
    np.float32([[100, 100], [400, 100], [100, 400], [400, 400]]),  # Destination for output 3
    np.float32([[50, 50], [250, 50], [50, 250], [250, 250]]),  # Destination for output 4
    np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])  # Destination for output 5
]

# Create a matplotlib figure with subplots
plt.figure(figsize=(15, 10))  # Enlarge the figure size for better visualization

# Plot the original input image
plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title('Input')
plt.xticks([]), plt.yticks([])

# Apply perspective transformations, plot and display the transformed images
for i, pts2 in enumerate(pts2_list):
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (300, 300))
    
    plt.subplot(2, 3, i + 2)
    plt.imshow(dst)
    plt.title(f'Output {i + 1}')
    plt.xticks([]), plt.yticks([])

# Display the matplotlib figure with all subplots
plt.tight_layout()
plt.show() """


""" import cv2
import numpy as np

# Read the input image
img = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 4\\images\\smarties.png')

# Define source and destination points for perspective transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[0, 0], [250, 0], [0, 250], [250, 250]])

# Calculate the perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation to the image
dst = cv2.warpPerspective(img, M, (250, 250))

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows() """



""" Averaging, in the context of image processing, refers to the process of smoothing or blurring an image by calculating the average value of pixel intensities in a local neighborhood around each pixel. This technique is used to reduce noise, suppress high-frequency details, and create a more visually coherent image. """

""" 
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 4\\images\\opencv.png')

# Apply a blur filter to the input image
# The blur filter helps in reducing noise and smoothing the image
blur = cv2.blur(img, (2, 2))  # Applying a blur filter with a kernel size of (5, 5)

# Create a matplotlib figure with subplots
plt.subplot(121)  # First subplot: original input image
plt.imshow(img)   # Display the original image
plt.title('Original')  # Title for the first subplot
plt.xticks([]), plt.yticks([])  # Hide x and y tick labels

plt.subplot(122)  # Second subplot: blurred image
plt.imshow(blur)  # Display the blurred image
plt.title('Blurred')  # Title for the second subplot
plt.xticks([]), plt.yticks([])  # Hide x and y tick labels

# Display the matplotlib figure with both subplots
plt.show()  # Display the figure containing both original and blurred images
# Don't forget to close the parentheses here """



""" import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('images/opencv.png')

# Apply Gaussian blur to the input image
# Gaussian blur is a type of image smoothing that reduces noise and preserves edges
blur = cv2.GaussianBlur(img, (5, 5), 0)
# The (5, 5) is the kernel size, and 0 is the standard deviation (not used in this case)

# Create a matplotlib figure with subplots
plt.subplot(121)  # First subplot: original input image
plt.imshow(img)   # Display the original image
plt.title('Original')  # Title for the first subplot
plt.xticks([]), plt.yticks([])  # Hide x and y tick labels

plt.subplot(122)  # Second subplot: Gaussian blurred image
plt.imshow(blur)  # Display the blurred image
plt.title('Blurred')  # Title for the second subplot
plt.xticks([]), plt.yticks([])  # Hide x and y tick labels

# Display the matplotlib figure with both subplots
plt.show()  # Display the figure containing both original and blurred images
# Don't forget to close the parentheses here """



import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('C:\\Suraj Sharma - Old PC\\School content\\School content\\IMAGE PROCESSING LEVEL 2\\Session 4\\images\\opencv.png')

# Apply Gaussian blur to the input image
blur = cv2.GaussianBlur(img, (5, 5), 20)
# Create a matplotlib figure with subplots
plt.figure(figsize=(12, 8))  # Set figure size for better visualization

# First row of subplots
plt.subplot(121)  # First subplot: Original image
plt.imshow(img)
plt.title('Original')
plt.xticks([]), plt.yticks([])

# First row of subplots
plt.subplot(122)  # First subplot: Original image
plt.imshow(blur)
plt.title('Original')
plt.xticks([]), plt.yticks([])

# Display the matplotlib figure with all subplots
plt.tight_layout()
plt.show()



""" Averaging:
Averaging, also known as box filtering or mean filtering, is a basic image smoothing technique. It reduces noise by replacing each pixel's value with the average value of its local neighborhood, defined by a kernel. Averaging helps in blurring the image and reducing high-frequency noise.

The formula for averaging is:

NewPixelValue = (Sum of pixel values in the kernel) / (Number of pixels in the kernel)
Averaging is simple and quick, but it can lead to blurring of edges and details, as it treats all pixels equally.

2. Gaussian Filtering:
Gaussian filtering is a more advanced form of image smoothing that uses a Gaussian function as the kernel. It provides better control over the blurring effect and preserves edges to a greater extent than simple averaging.

The Gaussian function is bell-shaped and emphasizes central pixels while diminishing the influence of pixels farther from the center. This results in a smoother image that retains important structures.


3. Median Filtering:
Median filtering is used to remove "salt and pepper" noise from an image. It replaces each pixel's value with the median value of its local neighborhood. Median filtering is effective at removing isolated, high-intensity noise pixels, while preserving edges and finer details.

4. Erosion and Dilation:
Erosion and dilation are fundamental morphological operations that process binary images (black and white images). They involve moving a small kernel over the image and modifying pixel values based on neighboring pixels within the kernel.

Erosion: Erosion shrinks the boundaries of the foreground (white) regions in a binary image. It replaces a pixel's value with the minimum value within the kernel. Erosion is useful for noise reduction and separating touching objects.

Dilation: Dilation expands the boundaries of the foreground regions. It replaces a pixel's value with the maximum value within the kernel. Dilation is used to connect broken parts of an object and to emphasize features.

5. Opening and Closing:
Opening and closing are compound morphological operations that involve a combination of erosion and dilation.

Opening: Opening is erosion followed by dilation. It's used to remove small noise while preserving object boundaries. It can also be used to separate objects that are close together.

Closing: Closing is dilation followed by erosion. It's used to close small gaps between objects while preserving object shapes. It can also be used to fill small holes within objects.

6. Morphological Gradient:
The morphological gradient represents the difference between a dilated image and an eroded image. It emphasizes object boundaries and helps to locate object edges. The gradient is useful for edge detection and segmentation tasks.

In summary, these image processing techniques provide various tools for filtering, noise reduction, edge detection, and object manipulation. The choice of technique depends on the specific task and the desired balance between noise reduction and preservation of image features.
 """