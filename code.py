# Install OpenCV
!pip install opencv-python

import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image = cv2.imread('test image.jpg')

# Resize the image (optional, depending on your image size)
image = cv2.resize(image, (400, 600))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Convert the image to RGB for display in matplotlib
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image with detected faces
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes for better visualization
plt.show()

# Print the number of faces detected
print(f"Number of faces detected: {len(faces)}")
