import cv2
import numpy as np

yakala = cv2.VideoCapture(0)

while(True):
    deger,kare = yakala.read()
    cv2.imshow("Ben",kare)
    a = cv2.waitKey(0)

    if a == 27:
        break

yakala.release()
cv2.destroyAllWindows()

#Burada yakala,deger,kare hepsi birer degiskendir.