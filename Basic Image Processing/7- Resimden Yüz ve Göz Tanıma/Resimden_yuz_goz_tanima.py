import cv2
import numpy as np

img = cv2.imread("kolpa.jpg",0)

def detectFaces_Eyes_FromImage(image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    img = cv2.imread(image)

    gray_scale =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_scale,1.2,1)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        roi_gray = gray_scale[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.imshow("asdaadad",img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
#detectFaces_Eyes_FromImage("unnamed.jpg")
#detectFaces_Eyes_FromImage("yuzler.jpg")
detectFaces_Eyes_FromImage("kolpa.jpg")
#detectFaces_Eyes_FromImage("YUZ.jpg")
#detectFaces_Eyes_FromImage("fifa.jpg")


