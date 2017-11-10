import cv2
img = cv2.imread('/home/linfangzhi/PycharmProjects/Machine_Learing/OpenCV/666.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('/home/linfangzhi/PycharmProjects/Machine_Learing/OpenCV/haarcascades/haarcascade_fullbody.xml')
face = face_cascade.detectMultiScale(
    gray,1.3,5
)
print('发现{0}个脸'.format(len(face)))
for (x,y,w,h) in face:
    cv2.circle(img,((x+x+w)//2,(y+y+h)//2),w//2,(0,0,255),2)
cv2.imwrite('14Peoele.jpg',img)
cv2.imshow('gray',img)
cv2.waitKey(0)