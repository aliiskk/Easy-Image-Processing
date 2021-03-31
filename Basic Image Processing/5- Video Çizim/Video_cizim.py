import cv2

cap = cv2.VideoCapture("yuruyeninsanlar.mp4")

while(cap.isOpened()):

    ret,frame = cap.read(1)
    frame = cv2.rectangle(frame,(500,250),(190,100),(0,255,0),5) #dikdortgen cizimi ve acilari
    cv2.imshow("video",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): #"q" tusu ile kapatma
        break

cap.release()
cv2.destroyAllWindows()