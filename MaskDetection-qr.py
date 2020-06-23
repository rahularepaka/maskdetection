import cv2
from playsound import playsound
import winsound
import numpy as np
from pyzbar.pyzbar import decode

detector = cv2.CascadeClassifier('hcs/haarcascade_frontalface_default.xml')  #Change the Location the file in your PC

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

count = 0
frameWidth = 640
frameHeight = 480


def qr():
    while True:

        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
            qr.var = myData
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 0, 255), 2)
            if myData == qr.var:
                cv2.rectangle(img, (0, 200), (640, 300),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Please Exit !! Scan is Successful", (90, 265), cv2.FONT_HERSHEY_DUPLEX,
                            1, (0, 0, 255), 2)
                

        cv2.imshow('Result', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


def maskdetectionprogram():
    while (True):
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 5)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)

        if faces is ():
            cv2.putText(img, "Good To Go!!", (200, 50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, qr.var, (270, 100),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)
            winsound.Beep(40, 100)
        else:
            
            masknotdet = cv2.putText(img, "NO MASK - PLEASE WEAR MASK", (200, 50),
                                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(img, qr.var, (270, 100),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)
            #winsound.Beep(5000, 100)
            savedimg = print(
                "Do You Want To Save The Person's Image then click Enter")
            count = 0
            if cv2.waitKey(1) & 0xFF == 13:
                cv2.imwrite(qr.var+str(count)+".jpg", imgRoi)
                count += 1
                cv2.rectangle(img, (0, 200), (640, 300),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                            2, (0, 0, 255), 2)

        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


qr()
maskdetectionprogram()
