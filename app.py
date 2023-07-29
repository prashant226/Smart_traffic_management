from flask import Flask, render_template
import cv2

app = Flask(__name__)

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
    ret, frame = cap.read()

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
            blue_vehicles += 1
        else:
            red_vehicles += 1

# Define a route to display the vehicle count
@app.route('/')
def vehicle_count():
    return render_template('count.html', blue=blue_vehicles, red=red_vehicles)

if __name__ == '__main__':
    app.run(debug=True)
