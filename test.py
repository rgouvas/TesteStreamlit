import numpy as np
import cv2
import utlis


################################################33
heightImg = 700
widthImg  = 700
path = "E:/Python_Trabalhos/1.jpg"


img = cv2.imread(path)
img =cv2.resize(img, (widthImg,heightImg))

imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur =cv2.GaussianBlur(imgGray,(5,5),1)

imgCanny = cv2.Canny(imgBlur,10,50)

imageArray = ([img,imgGray,imgBlur,imgCanny])

imgStacked = utlis.stackImages(imageArray,0.5)

#cv2.imshow("Original",img)
cv2.imshow("Stacked",imgStacked)
cv2.waitKey(0)




