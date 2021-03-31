import cv2
import numpy as np

img = cv2.imread("manzara.jpg",0) # 0=resmi siyah-beyaz yapar // # 1=default resim// # -1=alfa kanalı dahil olmak üzere yükler
cv2.imshow("ResimAdi",img)  #imshow komutu = imageshow = resmi gösterdir; ilk önce pencereye verilecek ad sonra da gösterilecek resim yazılır
cv2.waitKey(0)              # resmin kapanmamasını sağlar(ms)
cv2.destroyAllWindows()     # windowsta herhangi bir tuşa basıldıgında kapanması sağlar