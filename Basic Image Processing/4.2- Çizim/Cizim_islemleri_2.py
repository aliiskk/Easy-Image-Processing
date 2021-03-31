import cv2, sys
import numpy as

img = cv2.imread("bim.png")

img2=cv2.rectangle(img,(10,10),(202,86),(0,200,0),(5))

img3 = cv2.circle(img2,(202,86),40,(70,99,20),-1)
#cv2.imshow("bim_daire",img3)
font = cv2.FONT_HERSHEY_PLAIN
img4 = cv2.putText(img3,"python",(50,125),font,5,(0,0,0),5,cv2.LINE_AA)
cv2.imshow("yazili_resim",img4)

cv2.waitKey(0)
cv2.destroyAllWindows()

