import cv2
import numpy as np
from matplotlib import pyplot as plt # matplotlib kutuphanesi import edilip plt komutu yazılmıstır


img = cv2.imread("opencvlogo.png",0) # resmi okur ve siyah-beyaz şekilde yazdırır
plt.imshow(img,cmap="gray",interpolation="bicubic") # resim ,'gray' burada tanımlı renktir cmap ana resim rengini belirler("Blues" ile ana resim mavi olur)

plt.show()  # resmi matplotlib olarak çıkartır (grafik şeklinde)

