import cv2
import numpy as np

img = cv2.imread("bim.png")
#cv2.imshow("bim_penceresi",img)

img2=cv2.rectangle(img,(10,10),(202,86),(0,200,0),(5))
#cv2.imshow("bim_sb_penceresi",img2)

img3 = cv2.circle(img2,(202,86),40,(70,99,20),-1)
cv2.imshow("bim_daire",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

#-1 komutu daire ve dikdortgenin içini boyar
# opencv'de rengler R-G-B diye degil
# B-G-R DİYE GİDER (BLUE,GREEN,RED)