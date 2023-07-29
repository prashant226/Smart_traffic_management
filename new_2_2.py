import cv2

# Load the image from file
img = cv2.imread('image.jpg')
img = cv2.resize(img, (640, 480)) # resize the image to match the video frame size

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Loop over each frame in the video
while True:
    # Read the current frame from the video
    ret, frame = cap.read()

    # If the end of the video is reached, exit the loop
    if not ret:
        break

    # Resize the video frame to match the image size
    frame = cv2.resize(frame, (640, 480))

    # Convert the video frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the two frames side by side
    combined_frame = cv2.hconcat([img, gray])
    cv2.imshow('Combined frames', combined_frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
