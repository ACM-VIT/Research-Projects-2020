#importing libraries
import numpy as np
import cv2

#Applying the CascadeClassifier
face_cascade = cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/content/haarcascade_eye.xml')
   
#converting the image to grayscale
img = cv2.imread('/content/4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting the face
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#drawing the boxes
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #Detecting the eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)
    #drawing the boxes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
#displaying images        
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
