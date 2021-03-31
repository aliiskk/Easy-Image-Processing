import cv2
import numpy as np

catch = cv2.VideoCapture(0)

while(True):
    value,frame = catch.read()
    cv2.imshow("Kameram",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



catch.release()
cv2.destroyAllWindows

#catch,value,frame birer degiskendir.
#burada bilgisayarımızın kamerasını aktif hale getirip,"q" tuşu ile kapatmayı yaptık

