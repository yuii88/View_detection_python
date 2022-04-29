import cv2
faceCascade = cv2.CascadeClassifier("C://Users/CPE/Documents/code_i_vs/python/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("C://Users/CPE/Documents/code_i_vs/python/opencv/opencv-master/data/haarcascades/haarcascade_eye.xml")

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    #detext face
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords =[]
    #draw rectangle
    for (x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
        coords = [x,y,w,h]
    return img,coords

def detect(img,faceCascade,eyeCascade):
    img,coords = draw_boundary(img,faceCascade,1.1,10,(0,255,0),"Face")
    img,coords = draw_boundary(img,eyeCascade,1.1,12,(255,0,0),"Eye")
    return img


cap = cv2.VideoCapture("C://Users/CPE/Documents/code_i_vs/python/opencv/viewyDance.mp4")
while(True):
    ret,frame = cap.read()
    frame=detect(frame,faceCascade,eyeCascade)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

