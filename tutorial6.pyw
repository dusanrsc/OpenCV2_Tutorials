# importing modules
import cv2
import numpy

# reading and processing image
img = cv2.imread("assets/chessboard.png")
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
resized_img_and_grayscaled = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# tracking corners
corners = cv2.goodFeaturesToTrack(resized_img_and_grayscaled, 100, 0.01, 10)
corners = numpy.int64(corners)

# looping through corners and drawing circles on them
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# looping through corners and drawing lines to them
for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), numpy.random.randint(0, 255, size=3)))
		cv2.line(resized_img, corner1, corner2, color, 1)

# displaying image
cv2.imshow("Tutorial6", resized_img)

# destroying windows
cv2.waitKey(0)
cv2.destroyAllWindows()