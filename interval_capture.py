import cv2
from picamera2 import Picamera2
import numpy as np
import os
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera (optional, set resolution and format)
picam2.configure(picam2.create_still_configuration())

# Start the camera preview (captures frames)
picam2.start()

# Create a folder to save images if it doesn't exist
save_folder = 'captured_images'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Start capturing images every 10 seconds
last_capture_time = time.time()  # Initialize time

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Convert the frame from RGB (Picamera2 default) to BGR (OpenCV default)
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Resize the frame (optional, not required for saving)
    resized_frame = cv2.resize(frame_bgr, (320, 240))  # Resize to 320x240 for display

    # Display the resized frame
    cv2.imshow('Camera Feed (Resized)', resized_frame)

    # Get the current time
    current_time = time.time()

    # Capture and save an image every 10 seconds
    if current_time - last_capture_time >= 10:
        # Create a filename based on the current timestamp
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(save_folder, f"image_{timestamp}.jpg")

        # Save the frame as an image
        cv2.imwrite(filename, frame_bgr)

        print(f"Image saved as {filename}")

        # Update the last capture time
        last_capture_time = current_time

    # Check for key press to exit (press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
picam2.stop()
cv2.destroyAllWindows()
