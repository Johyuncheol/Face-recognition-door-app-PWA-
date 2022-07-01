import cv2
from cv2 import split
import numpy as np
from PIL import Image
import os
#import homomorphic as Hom
import pyrebase
import RPi.GPIO as GPIO
import time

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



# Path for face image database
path = 'dataset'
conf_threshold = 0.6

# load model
model_path = 'models/opencv_face_detector_uint8.pb'
config_path = 'models/opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
recognizer = cv2.face.LBPHFaceRecognizer_create()


# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")] #이미지만 포함하도록 필터링    
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath)#.convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        result_img = img_numpy.copy()
        h, w, _ = result_img.shape
        blob = cv2.dnn.blobFromImage(result_img, 1.0, (100, 100), [104, 117, 123], False, False)
        net.setInput(blob)

        # inference, find faces
        detections = net.forward()

        # postprocessing
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * w)
                y1 = int(detections[0, 0, i, 4] * h)
                x2 = int(detections[0, 0, i, 5] * w)
                y2 = int(detections[0, 0, i, 6] * h)

                gray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2GRAY)


                faceSamples.append(gray[y1:y2,x1:x2])
                ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faceSamples,ids = getImagesAndLabels(path)
recognizer.train(faceSamples, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
# Print the numer of faces trained and end program

print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

for i in range(2):
    GPIO.output(12, False)
    time.sleep(0.05)
    GPIO.output(12, True)
    time.sleep(1)