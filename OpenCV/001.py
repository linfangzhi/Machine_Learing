import cv2
import time

img = cv2.imread('/home/linfangzhi/PycharmProjects/Machine_Learing/OpenCV/timg.jpg')
a = time.time()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('/home/linfangzhi/PycharmProjects/Machine_Learing/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(
    gray,1.3,5
)
for (x,y,w,h) in face:
    cv2.circle(img,((x+x+w)//2,(y+y+h)//2),w//2,(255,255,255),3)
b = time.time()
print(b-a)
cv2.imshow('gray',img)
cv2.imshow('asd',gray)
cv2.waitKey(0)