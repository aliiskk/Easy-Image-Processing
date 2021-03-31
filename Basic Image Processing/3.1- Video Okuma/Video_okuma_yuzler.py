import cv2
import numpy as np

catch = cv2.VideoCapture("yuruyeninsanlar.mp4") # yuruyeninsanlar.mp4 videosu


while(catch.isOpened()):    #while dongusu icinde True veya False dondurur
    value,frame = catch.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Kameram",gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

catch.release()  #kamerayı serbest bırak
cv2.destroyAllWindows # açılan pencereleri kapat
