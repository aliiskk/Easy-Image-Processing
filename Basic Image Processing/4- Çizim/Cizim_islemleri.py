import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.imshow("Pencere_adi",img)

img2 = cv2.line(img,(0,0),(512,512),(255,0,0),20)
cv2.imshow("Pencere_cizgili",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()