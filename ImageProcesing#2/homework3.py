import cv2
import numpy as np

picture=cv2.imread("foto3.jpg",0)
cv2.imshow("normalphoto",picture)
max_picture=np.max(picture)         #most value of histogram
[height,weight]=np.shape(picture)

for i in range (0,height):
    for j in range (0,weight):
        picture[i,j]=max_picture-picture[i,j]       #subtract the current value from the maximum value

cv2.imshow("invertphoto",picture)
cv2.waitKey()

