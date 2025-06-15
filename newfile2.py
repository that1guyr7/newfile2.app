import cv2,os
import numpy as np

# diamond = cv2.imread("Assets/diamond addition.jpeg")
# star = cv2.imread("Assets/star addition.jpeg")
# bobby = cv2.imread("Assets/bobby.png")

#add = cv2.addWeighted(star,0.9,diamond,1,0)
#cv2.imshow("bob+",add)
#cv2.waitKey(0)

#subtract = cv2.subtract(diamond,star)
# cv2.imshow("bob-",subtract)
# cv2.waitKey(0)

# bobbyresize = cv2.resize(bobby,(500,500))
# cv2.imshow("bob++",bobbyresize)
# cv2.waitKey(0)

# Gaussian Blur - used mostly in machine learning preprocessing steps  
# Median Blur - used in digital processing preserves edges but removes noise 
# Bilateral Blur - only sharp edges are preserved here

# bilateral = cv2.imread("Assets/bilateral.jpg")
# saltandpeppergrains = cv2.imread("Assets/salt and pepper grains.jpeg")

# gaussianblur = cv2.GaussianBlur(bilateral,(101,101),0,0)
# cv2.imshow("bob+++",gaussianblur)
# cv2.waitKey(0)

# medianblur = cv2.medianBlur(saltandpeppergrains,7)
# cv2.imshow("bob++++",medianblur)
# cv2.waitKey(0)

# bilateralfilter = cv2.bilateralFilter(bilateral,7,101,101)
# cv2.imshow("bob+++++",bilateralfilter)
# cv2.waitKey(0)

# medianblur = cv2.medianBlur(median,7,9,10)
# cv2.imshow("bob+++++",medianblur)
# cv2.waitKey(0)

pika = cv2.imread("Assets/pika.png")
# border = cv2.copyMakeBorder(people,50,50,50,50,cv2.BORDER_REPLICATE)
# cv2.imshow("bob++++++",border)
# cv2.waitKey(0)
kernel = np.ones((100,100),np.uint8)
erosion = cv2.erode(pika,kernel)
cv2.imshow("bob+++++++",erosion)
cv2.waitKey(0)
