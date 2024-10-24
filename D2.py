import cv2
import numpy as np

img = cv2.imread('/home/ilkham/Penugasan GamaForce/folder_image/Just Do It.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("inilagi", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()