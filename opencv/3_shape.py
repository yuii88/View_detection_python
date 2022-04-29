import cv2
#img = cv2.line(img,(0,0),(255,255),(0,0,255),10) #line
#img = cv2.arrowedLine(img,(0,0),(400,400),(255,0,0),5) #arrow
#img = cv2.rectangle(img,(370,0),(200,200),(0,0,255),10) # rectangle
#img = cv2.circle(img,(200,63),40,(0,255,0),-1) # circle

#img =cv2.putText(img,"OpenCV",(30,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) #TEXT
#input
img = cv2.imread("C://Users/CPE/Documents/code_i_vs/python/opencv/view1.jpg",1)

img =cv2.putText(img,"OpenCV",(30,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow("Result",img)

cv2.waitKey(0)
cv2.destroyAllWindows()