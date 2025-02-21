import numpy as np
import cv2

img = cv2.resize(cv2.imread('C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('C:\\Users\\OMOLP094\\Desktop\\Image Processing - Level 2\\Image Processing (OpenCV) Course\\Images\\ball.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape # getting the height & width of the template image

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# list of all the methods that are used for template matching, we can try all the methods & see which one works best & then continue using that one

for method in methods: # looping through all the methods
    img2 = img.copy() # we need to create a copy of the image for every method that we are using for template matching, if we don't create a copy then we would end up drawing multiple boxes for detecting the object in the same image

    result = cv2.matchTemplate(img2, template, method)
# matchTemplate method performs convolution which basically means it takes the template image & slides it over the entire base image & checks which region of the base image is the closest match for the template image, a 2D array would be returned indicating how close of a match is a particular region of the base image with our template image

# Dimension of the result 2D array : (W - w + 1, H - h + 1)
# W, H - width & height of the base image

# w, h - width & height of the template image

# e.g. base image - 4*4 & template image - 2*2
# W, H = 4, 
# w, h = 2
# result matrix - w - 3, h - 3 

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # gives the min, max value & location of the min & max value of the result array 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc # minimum difference score
    else:
        location = max_loc # maximum similarity score

# Difference-Based Methods (cv2.TM_SQDIFF and cv2.TM_SQDIFF_NORMED):

# These methods are based on calculating the squared differences between the template and the image.
# In these methods, a lower similarity score (lower squared difference) indicates a better match. In other words, a match with a lower difference is considered more similar.
# Therefore, the location of the best match for these methods is determined by min_loc, which corresponds to the location with the minimum squared difference. This is because a smaller value indicates a better match.

# Other Methods:

# For all other template matching methods (cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, and cv2.TM_CCORR_NORMED), higher similarity scores represent better matches.
# In these methods, a higher value indicates a stronger correlation or similarity between the template and the image.
# Therefore, the location of the best match for these methods is determined by max_loc, which corresponds to the location with the maximum similarity score. This is because a larger value indicates a better match.

    bottom_right = (location[0] + w, location[1] + h) # w, h are being added to the x, y coordinates of the top left corner of the match in the base image to get the bottom right corner
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



""" 
Image Loading and Resizing:

Two grayscale images are loaded using cv2.imread from image files: 'soccer_practice.jpg' and 'shoe.PNG'.
Both images are resized using cv2.resize with a scaling factor of 0.8 to reduce their size by 20%. The resized images are stored in the variables img (soccer practice scene) and template (shoe template).
Template Matching Methods:

A list of template matching methods is defined in the methods variable. These methods are provided by OpenCV for template matching.
Loop Over Methods:

The code iterates through each template matching method in the methods list using a for loop.
Template Matching:

Inside the loop, a copy of the original image (img2) is created using img.copy() to avoid modifying the original image in each iteration.
The cv2.matchTemplate function is used for template matching. It takes three parameters:
img2: The larger image (soccer practice scene).
template: The smaller template image (shoe).
The current template matching method from the methods list.
The result of the template matching operation is stored in the result variable. This result is essentially a heat map indicating the degree of similarity between the template and the image.
Locating the Template:

After template matching, the code uses cv2.minMaxLoc to find the location of the best match within the result heat map. This function provides:
min_val: The minimum similarity score (not used in this code).
max_val: The maximum similarity score, indicating the strength of the match.
min_loc: The location of the minimum value (not used in this code).
max_loc: The location of the maximum value, which corresponds to the top-left corner of the detected template match.
Drawing a Rectangle:

A rectangle is drawn around the detected template match using the cv2.rectangle function. The rectangle is drawn on the img2 copy.
The location obtained from the previous step represents the top-left corner of the rectangle, and the dimensions of the rectangle are determined by the width (w) and height (h) of the template image.
The rectangle is drawn in white (color value 255) with a line thickness of 5 pixels.
Displaying the Result:

The image with the drawn rectangle highlighting the detected template match is displayed using cv2.imshow.
The code then waits for a key press using cv2.waitKey(0), allowing you to see the result for each matching method before proceeding to the next one.
After you press any key, the displayed window is closed using cv2.destroyAllWindows().
Cleanup:

After processing all template matching methods, the program waits for a key press and then closes all displayed windows. """


# Template Matching For Video : 
""" 
import numpy as np
import cv2

# Load the video file (replace 'video_file.mp4' with your video file)
cap = cv2.VideoCapture('video_file.mp4')

# Load the template image
template = cv2.imread('assets/shoe.PNG', 0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    for method in methods:
        img2 = frame.copy()

        # Perform template matching
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        # Define the region of interest (ROI) for the detected object
        top_left = location
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw a rectangle around the detected object
        cv2.rectangle(img2, top_left, bottom_right, 255, 5)

        # Display the result
        cv2.imshow('Object Detection', img2)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows() """
