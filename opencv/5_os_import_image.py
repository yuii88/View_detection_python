import numpy as np
from PIL import Image
import os,cv2

def train_classifier(data_dir):
    data_dir="C://Users/CPE/Documents/code_i_vs/python/opencv/data"
    path = [os.path.join (data_dir,f) for f in os.listdir(data_dir) ] # input location file image
    faces=[]
    ids=[]

    for image in path:
        img=Image.open(image).convert("L") # convert image to grayscale
        imageNp =np.array(img,'uint8') # unit8 = 8 bits (grayscale)
        id =int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)

    ids=np.array(ids)

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")

    

#data_dir="C://Users/CPE/Documents/code_i_vs/python/opencv/data"
train_classifier("data")