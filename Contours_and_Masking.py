import numpy as np
import cv2

# Open the webcam capture
cap = cv2.VideoCapture(0)

# Set the width and height of the capture
cap.set(3, 640)
cap.set(4, 480)

# Set the brightness level
cap.set(10, 300)

# Define kernels for morphological operations
kernel_e = np.ones((7, 7), np.uint8)
kernel_d1 = np.ones((5, 5), np.uint8)
kernel_d2 = np.ones((3, 3), np.uint8)

# Initialize an empty list to store detected points
points = []

# Loop to process frames from the webcam
while True:
    # Capture a frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of blue color in HSV
    lower_blue = np.array([26, 53, 0])
    upper_blue = np.array([79, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through detected contours
    for cnt in contours:
        if cv2.contourArea(cnt) > 800:
            # Approximate the contour to a polygon
            epsilon = 0.02 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            x, y, w, h = cv2.boundingRect(approx)
            
            # Draw a rectangle around the detected object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            
            # Mark the top center point of the detected object
            cv2.circle(frame, (((x + (x + w)) // 2), y), 4, (0, 0, 255), -1)
            
            # Add the top center point to the list of points
            points.append([((x + (x + w)) // 2), y])
            
    # Draw circles at the recorded points
    for p in points:
        cv2.circle(frame, (p[0], p[1]), 4, (0, 0, 255), -1)
    
    # Display the frame with annotations
    cv2.imshow('frame', frame)
    
    # Check for the 'Esc' key press to exit the loop
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()


# The code starts by importing necessary libraries and initializing the webcam capture using cv2.VideoCapture(0).

# It sets the width and height of the capture using the set() function.

# The brightness level is adjusted using the set() function with the parameter 10.

# Kernels for morphological operations (erosion and dilation) are defined to be used later.

# An empty list named points is created to store the top center points of the detected blue objects.

# Inside the main loop, the code captures a frame from the webcam and flips it horizontally for more natural interaction.

# The frame is converted from BGR color space to HSV color space, which is better for color-based segmentation.

# A range for blue color in the HSV space is defined using lower_blue and upper_blue.

# The code applies a mask using cv2.inRange() to extract blue objects from the frame.

# Contours are detected using cv2.findContours() in the mask.

# The code loops through the detected contours and checks if the contour area is larger than a threshold. If it is, the code approximates the contour with a polygon and draws a rectangle around the detected object.

# The top center point of the detected object is marked with a red circle using cv2.circle().

# The top center point is added to the points list for tracking.

# The code then draws red circles at all the recorded points.

# The frame with annotations is displayed using cv2.imshow().

# The code waits for the 'Esc' key to be pressed (k == 27) to exit the loop.

# After exiting the loop, the webcam is released using cap.release() and all OpenCV windows are closed using cv2.destroyAllWindows().