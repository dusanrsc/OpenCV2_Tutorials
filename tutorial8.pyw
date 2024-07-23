# importing modules
import cv2
import numpy

# reading video image from camera
cap = cv2.VideoCapture(0)

# importing detection classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# main program loop
while True:

	# returning success and frame
	ret, frame = cap.read()

	# converting video capture in grayscale
	grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# face detection
	faces = face_cascade.detectMultiScale(grayscale, 1.3, 5)

	# looping through face detection
	# separation of positions and sizes of the face/s
	for (x, y, width, height) in faces:

		# draw rectangle on face
		cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 5)

		# roi = region of interest
		# if finded face, find eyes on the face
		roi_gray = grayscale[y : y + width, x : x + width]
		roi_color = frame[y : y + width, x : x + width]

		# eyes detection
		eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

		# drawing rectangle on eyes
		for (eye_x, eye_y, eye_width, eye_height) in eyes:
			cv2.rectangle(roi_color, (eye_x, eye_y), (eye_x + eye_width, eye_y + eye_height), (0, 255, 0), 5)

	# displaying the video image
	cv2.imshow("Tutorial 8", frame)

	# destroying the window if specific key (event) is pressed
	if cv2.waitKey(1) == ord("q"):
		break

# liberating camera source for other programs
cap.release()

# destroying windows
cv2.destroyAllWindows()