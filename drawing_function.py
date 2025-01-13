import numpy as np
import cv2

img = cv2.imread('lena.png')
img = cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(147,50,0),3)
img = cv2.arrowedLine(img,(0,255), (255,400),(255,255,0),3)

cv2.imshow('lena.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()