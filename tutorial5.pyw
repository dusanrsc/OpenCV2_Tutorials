# importing modules
import cv2
import numpy

# reading video image from camera
cap = cv2.VideoCapture(0)

# main program loop
while True:
	# returning success and frame
	ret, frame = cap.read()

	# creating width and height variable
	width = int(cap.get(3))
	height = int(cap.get(4))

	# converting color channels of video image
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = numpy.array([50, 90, 50])
	upper_blue = numpy.array([255, 150, 255])

	# creating a mask
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# compare images with bitwise function
	# compare images and not showing except green color
	result = cv2.bitwise_and(frame, frame, mask=mask) 

	# displaying the video image
	cv2.imshow("Tutorial5", result)

	# destroying the window if specific key (event) is pressed
	if cv2.waitKey(1) == ord("q"):
		break

# liberating camera source for other programs
cap.release()

# destroying windows
cv2.destroyAllWindows()