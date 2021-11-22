import numpy as np
import cv2


#load color image
img1 = cv2.imread("/home/pi/Pictures/tokyo.jpg")

# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
# flipThresh = cv2.flip(thresh, 0)
# 
# cv2.imshow("potato", flipThresh)

w = int(img1.shape[1]*100/100)
h = int(img1.shape[0]*100/100)
dim = (w,h)


        
#filtering
x = 3
#kernel = np.ones((x,x),np.uint8)

#if ((x%2)==0):
#         x = x+1

blur = cv2.GaussianBlur(img1,(x,x),0)

for _ in  range(1):
    img1 = cv2.Laplacian(blur, cv2.CV_64F)

image = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("potato", image)


#Keep the window open until the user presses a key
cv2.waitKey(0)

    
cv2.destroyAllWindows()



