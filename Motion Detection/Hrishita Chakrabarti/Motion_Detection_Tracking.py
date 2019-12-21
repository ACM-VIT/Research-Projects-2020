import cv2
import numpy as np

cap = cv2.VideoCapture("Vtest.avi")
ret, frame1 = cap.read()
ret, frame2  = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0) #remove noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #converts images into binary images (contextually: foreground and background)
    dilated = cv2.dilate(thresh, None, iterations = 3) #fill up black spots for better analysis
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #finding the contours of the refined images

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) #w: width, h: height

        if(cv2.contourArea(contour) < 900): #we are ignoring smaller motions like those of ropes
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: (Movement)", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()