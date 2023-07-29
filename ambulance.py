import cv2

# Load the pre-trained Haar Cascade classifier for vehicles
vehicle_cascade = cv2.CascadeClassifier('emergency.xml')

# Load the input video
cap = cv2.VideoCapture('highway.mp4')

# Loop over each frame in the video
while True:
    # Read the current frame from the video
    ret, frame = cap.read()

    # If the end of the video is reached, exit the loop
    if not ret:
        break

    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the current frame using the Haar Cascade classifier
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected vehicles in the current frame with blue color
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # blue color tuple (r, g, b) = (255, 0, 0)

    # Display the current frame with detected vehicles
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

