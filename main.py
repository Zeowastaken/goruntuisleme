import cv2
import numpy as np

photo = cv2.imread("umbrella.jpg", 0) #upload to photo
cv2.imshow("umbrella", photo)
cv2.waitKey()

histogram = np.zeros(256)
[a, b] = np.shape(photo)
for x in range(0, a): #axb is pixel numbers of picture
    for y in range(0, b):
        z = photo[x, y]
        histogram[z] = histogram[z] + 1 #pass to next pixel to check

for x in range(0, 256):
    print(x, "->", histogram[x])

    #designed by zeo