# importing modules
import cv2
import random

# reading image
img = cv2.imread("assets/soccer_practice.jpg", -1)

# looping trough the image
for i in range(0, 100):
	for j in range(0, 100):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# croping image
crop = img[90:140, 200:300]

# pasting croped on image
# note that the size of the croped and pasted must be the same
img[215:265, 180:280] = crop
img[215:265, 300:400] = crop

# displaying image on the screen
cv2.imshow("Tutorial2", img)

# destroying windows
cv2.waitKey(0)
cv2.destroyAllWindows()