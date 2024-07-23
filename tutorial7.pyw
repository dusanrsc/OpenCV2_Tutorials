# importing modules
import cv2

# computer vision template matching methods
template_matching_methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# reading images as grayscale
img = cv2.imread("assets/soccer_practice.jpg", 0)
template = cv2.imread("assets/ball.PNG", 0)

# processing (resizing) images
img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
template_resized = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)

# gathering height and width of image
height, width = template_resized.shape

# looping through template matching methods
for method in template_matching_methods:
	# creating copy of image
	img2 = img_resized.copy()

	# displaying matches
	result = cv2.matchTemplate(img2, template_resized, method)
	min_value, max_value, min_location, max_location = cv2.minMaxLoc(result)

	# checking if method is in specific template matching methods
	# "location" is the top left coordinate
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_location
	else:
		location = max_location

	# bottom right coordinate
	bottom_right = (location[0] + width, location[1] + height)

	# black color code for grayscale color channel
	color = 255

	# draw rectangle on locations
	cv2.rectangle(img2, location, bottom_right, color, 5)

	# displaying image on the screen
	cv2.imshow("Tutorial7", img2)

	# destroying the window by key (event) press
	if cv2.waitKey(0) == ord("q"):
		break

# destroying windowss
cv2.destroyAllWindows()