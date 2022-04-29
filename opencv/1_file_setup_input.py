import cv2

#input from image 
#img = cv2.imread("C://Users/CPE/Documents/code_i_vs/python/opencv/view1.jpg",0)
# cv2.imshow('Show Result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('result.png',img)

#====================================

#input from camera 
# cap = cv2.VideoCapture(0)
# while(True):
#     ret,frame = cap.read()
#     cv2.imshow('frame',frame)
#     if(cv2.waitKey(1) & 0xFF==ord('q')):
#         break
# cap.release()
# cv2.destroyAllWindows()

#====================================

#input from video
# cap = cv2.VideoCapture("C://Users/CPE/Documents/code_i_vs/python/opencv/viewyDance.mp4")
# while(True):
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     if(cv2.waitKey(1) & 0xFF==ord('q')):
#         break
# cap.release()
# cv2.destroyAllWindows()