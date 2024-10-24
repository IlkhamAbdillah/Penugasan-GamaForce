import cv2
import numpy as np

gambar = cv2.imread('/home/ilkham/Penugasan GamaForce/folder_image/Object Tracking.png')
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1,100, param1=200, param2=50, minRadius=50, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.drawMarker(gambar, (i[0], i[1]), (255,0,0), cv2.MARKER_CROSS, 30, 2)
    cv2.rectangle(gambar, (i[0]-108, i[1]-108), (i[0]+108, i[1]+108), (0,255,0), 2)
    cv2.rectangle(gambar, (i[0]-338, i[1]-338), (i[0]+338, i[1]+338), (0,0,255), 2, )

cv2.imshow("inidia", gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()