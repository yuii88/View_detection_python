from unittest import result
import cv2
faceCascade = cv2.CascadeClassifier("C://Users/CPE/Documents/code_i_vs/python/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
def create_dataset(img,id,img_id):
    cv2.imwrite("C://Users/CPE/Documents/code_i_vs/python/opencv/data/pic."+str(id)+"."+str(img_id)+".jpg",img)


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

def detect(img,faceCascade,img_id):
    img,coords = draw_boundary(img,faceCascade,1.1,10,(0,255,0),"Face")
    id = 1
    if len(coords)==4:
        #img(y:y+h,x:x+w)
        id=1
        result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        create_dataset(result,id,img_id)
    return img

img_id = 0
cap = cv2.VideoCapture("C://Users/CPE/Documents/code_i_vs/python/opencv/viewyDance.mp4")
while(True):
    ret,frame = cap.read()
    frame=detect(frame,faceCascade,img_id)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    img_id+=1
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

