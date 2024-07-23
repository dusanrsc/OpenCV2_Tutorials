# importing module
import cv2

# reading video image from camera
cap = cv2.VideoCapture(0)

# main program loop
while True:
	# returning success and frame
	ret, frame = cap.read()

	# creating width and height variable
	width = int(cap.get(3))
	height = int(cap.get(4))

	# drawing line over the image
	img = cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 5)

	# drawing circle over the image
	img = cv2.circle(frame, (250, 250), (50), (255, 255, 0), -1)

	# drawing rectangle over the image
	img = cv2.rectangle(frame, (0, 0), (200, 300), (0, 255, 0), 5)

	# drawing text over the image
	font = cv2.FONT_HERSHEY_SIMPLEX
	img = cv2.putText(frame, "Tutorial4", (0, 50), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

	# displaying the video image
	cv2.imshow("Tutorial4", frame)

	# destroying the window by key pressing
	if cv2.waitKey(1) == ord("q"):
		break

# liberating camera source for other programs
cap.release()

# destroying windows
cv2.destroyAllWindows()