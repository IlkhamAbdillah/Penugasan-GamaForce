import cv2
import numpy as np
import math

for i in range (0, 128):
    for j in range (0, 127):
        distance = math.sqrt((127-i)**2 + (127-j)**2)
        pixel = np.ones((1, 1, 3), np.uint8) * distance/255
        if(j==0):
            a = pixel
        else:
            a = np.hstack([a, pixel])
            
    isi = np.ones((1, 1, 3), np.uint8) * math.sqrt((127-i)**2)/255
    balik = np.flip(a)
    a = np.hstack([a, isi, balik])
    
    if(i==0):
        gambar = a
    else:
        gambar = np.vstack([gambar, a])
    if(i==126):
        balik_gambar = np.flip(gambar)
        
gambar = np.vstack([gambar, balik_gambar])

# x = 254
# y = 254

# cek_pixel = gambar[x, y]

# blue = cek_pixel[0]
# green = cek_pixel[1]
# red = cek_pixel[2]

# print(f"B={blue}, G={green}, R={red}")

cv2.imshow("tes", gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()