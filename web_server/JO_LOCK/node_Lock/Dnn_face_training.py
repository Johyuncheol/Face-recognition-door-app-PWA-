import cv2
from cv2 import split
import numpy as np
from PIL import Image
import os
import homomorphic as Hom
import firebase_admin
from uuid import uuid4
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import sys


bucket = storage.bucket()#기본 버킷 사용
ref = db.reference() #db 위치 지정, 기본 가장 상단을 가르킴



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

                #gray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2GRAY)
                gray = Hom.homo(img_numpy)

                faceSamples.append(gray[y1:y2,x1:x2])
                ids.append(id)
                # faceSamples.append(v2[y1:y2,x1:x2])
                #ids.append(id)
                #faceSamples.append(y[y1:y2,x1:x2])
                #ids.append(id)
    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faceSamples,ids = getImagesAndLabels(path)
recognizer.train(faceSamples, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
# Print the numer of faces trained and end program

blob = bucket.blob('trainer.yml')
new_token = uuid4()
metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
blob.metadata = metadata

#upload file
blob.upload_from_filename(filename='trainer/trainer.yml', content_type='yml')


print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
db.reference("도어락/파일다운").set('on')
db.reference("도어락/얼굴학습").set('off')
sys.exit(0)