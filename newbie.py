import cv2

# Load the pre-trained Haar Cascade classifier for vehicles
vehicle_cascade = cv2.CascadeClassifier('emergency.xml')

# Load the input video
cap = cv2.VideoCapture('highway.mp4')

# Initialize vehicle counters for blue and red frames
blue_vehicles = 0
red_vehicles = 0

# Loop over each frame in the video
while True:
    # Read the current frame from the video
    ret, frame = cap.read()q

    # If the end of the video is reached, exit the loop
    if not ret:
        break

    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the current frame using the Haar Cascade classifier
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected vehicles in the current frame with blue or red color depending on their x-coordinate
    for (x, y, w, h) in vehicles:
        if x < frame.shape[1] // 2:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # blue color tuple (r, g, b) = (255, 0, 0)
            blue_vehicles += 1
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # red color tuple (r, g, b) = (0, 0, 255)
            red_vehicles += 1

    # Display the current frame with detected vehicles and vehicle count
    cv2.putText(frame, f'Blue Vehicles: {blue_vehicles}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f'Red Vehicles: {red_vehicles}', (frame.shape[1] // 2 + 20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
