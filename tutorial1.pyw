# importing module
import cv2

# mode for image reading channel
# -1 / cv2.IMREAD_COLOR
#  0 / cv2.IMREAD_GRAYSCALE
#  1 / cv2.IMREAD_UNCHANGED - with alpha value included

# reading image
img = cv2.imread("assets/ball.PNG", 0)

# resizing image
#img = cv2.resize(img, (0, 0), fx=1, fy=1)

# rotating image
#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# saving (new) image
cv2.imwrite("assets/new_img.jpg", img)

# displaying image on the screen
cv2.imshow("Tutorial1", img)

# destroying windows
cv2.waitKey(0)
cv2.destroyAllWindows()