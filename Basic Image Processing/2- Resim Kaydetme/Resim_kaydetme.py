import cv2
import numpy as np

resim = cv2.imread("opencvlogo.png",0) # 0=resmi gri yapar // # 1=varsayılan olarak gelir resim aynı kalır // # -1=alfa kanalı dahil olmak üzere yükler
cv2.imshow("ResimAdi",resim)

# // RESMİ GRİ ŞEKİLDE KAYDETMEK //
# // Aşağıda ki kod resmi gri şekilde kaydeder.

# // cv2.imwrite("opencv_logosu_sb.png",resim) //  imwirte = imagewrite = resmi kaydeder

# \\ RESMİ TUŞ İLE KAPATIP KAYDETMEK
# \\ BURADA RESİM ESC TUSU İLE KAPANIR S TUSU İLE KAYDOLUR.

a = cv2.waitKey(0)
if a == 27:         # 27 BURADA ESC TUŞUNUN HEXEDECIMAL KARSILIGIDIR
    cv2.destroyAllWindows()  # herhangi bir tuşa basıldıgından kapanma kodu esc'ye aktarılmıstır
elif a == ord("s"):
    cv2.imwrite("open_s_tusu.png",resim)  #resmi "s" tusuna basıldıgında oldugu dosyaya kaydeder