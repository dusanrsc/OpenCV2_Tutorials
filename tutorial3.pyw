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

	# filling current image with black color
	image = numpy.zeros(frame.shape, numpy.uint8)

	# resizing video frame by 2 by x and y axes
	smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

	# displaying the all four video frames
	image[:height//2, :width//2] = smaller_frame # cv2.rotate(smaller_frame, cv2.ROTATE_180)
	image[height//2:, :width//2] = smaller_frame
	image[:height//2, width//2:] = smaller_frame # cv2.rotate(smaller_frame, cv2.ROTATE_180)
	image[height//2:, width//2:] = smaller_frame

	# displaying the video image
	cv2.imshow("Tutorial3", image)

	# destroying the window by key pressing
	if cv2.waitKey(1) == ord("q"):
		break

# liberating camera source for other programs
cap.release()

# destroying windows
cv2.destroyAllWindows()