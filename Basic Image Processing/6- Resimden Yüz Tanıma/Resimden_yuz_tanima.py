import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread("yuzler.jpg",0) #0 yazıp sb yaptım

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
yuzler = face_cascade.detectMultiScale(resim,1.2,5)

for(x,y,w,h) in yuzler:
    cv2.rectangle(resim,(x,y),(x+w,y+h),(0,0,255),5)

def detectFromImage(image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    resim = cv2.imread(image)
    resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    yuzlerim = face_cascade.detectMultiScale(resim,1.2,5)

    for(x,y,w,h) in yuzlerim:
        cv2.rectangle(resim,(x,y),(x+w,y+h),(255,255,255),4)
    cv2.imshow("Yuz tanima",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectFromImage("yuzler.jpg")






