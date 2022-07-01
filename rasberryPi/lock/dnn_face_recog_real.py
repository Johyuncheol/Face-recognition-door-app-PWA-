import cv2
import numpy as np
import os, time
from uuid import uuid4
from datetime import datetime
import pyrebase
import sys
import RPi.GPIO as GPIO
import importlib

#import homomorphic as Hom
config = {     
    "apiKey": "AIzaSyAYN_pMYdHba9tVYj_0XYPoRYXetZvevBw",
    "authDomain": "lock-2674d.firebaseapp.com",
    "databaseURL": "https://lock-2674d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "lock-2674d",
    "storageBucket": "lock-2674d.appspot.com",
    "messagingSenderId": "130079254258",
    "appId": "1:130079254258:web:ca22eac6546f91eb1c926b",
    "measurementId": "G-K2ZFQVJY2X"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


# load model
model_path = 'models/opencv_face_detector_uint8.pb'
config_path = 'models/opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
count=0
count1=0
pic_count=0
conf_threshold = 0.6
unknown_face=0
total_com=0
known_face=0


known_face = db.child("총인원").child("확인된").get().val()
unknown_face = db.child("총인원").child("미확인").get().val()
total_com = db.child("총인원").child("전체").get().val()
print(known_face ,unknown_face, total_com)


names=[]
name = db.child("등록자이름").get().val()
names = name
print(name)
print(len(name))



cam = cv2.VideoCapture(0)
cam.set(3, 640) # video widht
cam.set(4, 480) # video height

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

frame_count = 0  

while True:
    ret, img =cam.read()


    frame_count += 1

    start_time = time.time()
    
    # prepare input
    result_img = img.copy()
    h, w, _ = result_img.shape
    blob = cv2.dnn.blobFromImage(result_img, 1.0, (300, 300), [104, 117, 123], False, False)
    net.setInput(blob)

    # inference, find faces
    detections = net.forward()

    #gray=Hom.homo(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * w)
            y1 = int(detections[0, 0, i, 4] * h)
            x2 = int(detections[0, 0, i, 5] * w)
            y2 = int(detections[0, 0, i, 6] * h)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), int(round(h/150)), cv2.LINE_AA)
            id, confidence = recognizer.predict(gray[y1:y2,x1:x2])
            if ( ((confidence < 40 )and((confidence >= 40 ))) or (confidence < 40 )):
                
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                
                count1+=1
                if (count1%20 == 0):
                    now = datetime.now().strftime("%Y%m%d_%H%M%S")
                    print(now)
                    cv2.imwrite("Images/"+now + ".jpg", result_img)

                    #업로드할 파일명
                    uploadfile = "Images/"+now+".jpg"
                    #업로드할 파일의 확장자 구하기
                    s = os.path.splitext(uploadfile)[1]
                    #업로드할 새로운파일이름
                    filename = now + s 


                    #Upload files to Firebase
                    storage = firebase.storage()
                    storage.child("known/"+filename).put(uploadfile)
                    
                    url="https://firebasestorage.googleapis.com/v0/b/lock-2674d.appspot.com/o/known%2F"+now+".jpg"+"?alt=media"
                    

                    known_face+=1
                    db.child("등록자사진").child(known_face).set(url)

                    total_com+=1
                    db.child("전체사진").child(total_com).set(url)

                    db.child("총인원").child('확인된').set(known_face)

                    db.child("총인원").child('전체').set(total_com)
                
                    #도어락 제어
                    # GPIO.output(door,GPIO.HIGH)
                    # time.sleep(0.5)
                    # GPIO.output(door,GPIO.LOW)
                    GPIO.setwarnings(False)
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(12, GPIO.OUT)
                    GPIO.output(12, False)
                    time.sleep(1)
                    GPIO.output(12, True)
                    
                    pic_count=3
                    break

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                count+=1
                if (count%25 == 0):
                    
                    ['socket_client.py','who']
                    
                    pic_count+=1
                    now = datetime.now().strftime("%Y%m%d_%H%M%S")
                    print(now)
                    cv2.imwrite("Images/"+now + ".jpg", result_img)
                    

                    #업로드할 파일명
                    uploadfile = "Images/"+now+".jpg"
                    #업로드할 파일의 확장자 구하기
                    s = os.path.splitext(uploadfile)[1]
                    #업로드할 새로운파일이름
                    filename = now + s 


                    #Upload files to Firebase
                    storage = firebase.storage()
                    storage.child("unknown/"+filename).put(uploadfile)
                    
                    url="https://firebasestorage.googleapis.com/v0/b/lock-2674d.appspot.com/o/unknown%2F"+now+".jpg"+"?alt=media"


                    unknown_face+=1
                    db.child("미확인사진").child(unknown_face).set(url)

                    total_com+=1
                    db.child("전체사진").child(total_com).set(url)

                    db.child("총인원").child('미확인').set(unknown_face)

                    db.child("총인원").child('전체').set(total_com)
                    db.child("도어락").child('미확인시도알림').set('on')
                    
                    break
         
            cv2.putText(img, str(id), (x1,y1), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x1,y2), font, 1, (255,255,0), 1)


    

    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break
    if pic_count%3==0 and pic_count != 0:
        break


#print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()