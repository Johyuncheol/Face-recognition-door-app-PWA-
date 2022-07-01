import cv2, time
import pyrebase 


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



# 텐서플로우에서 학습된 모델을 사용
model_path = 'models/opencv_face_detector_uint8.pb' #훈련된 가중치
config_path = 'models/opencv_face_detector.pbtxt'  # 네트워크 구성 
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

conf_threshold = 0.6 #기준값 이하면 무시

# initialize video source, default 0 (webcam)
cap = cv2.VideoCapture(0)

frame_count, tt = 0, 0
count=0


names=[]
name = db.child("등록자이름").get().val()
names = name
print(name)

print(len(name))
db.child("총인원").child('등록자수').set(len(name)-1)
face_id = len(name)-1  ## 0번째는 none으로 할거임
print("\n [INFO] Initializing face capture. Look the camera and wait ...")


while(True):
  ret, img = cap.read()
  if not ret:
    break

  frame_count += 1

  start_time = time.time()

  # prepare input
  result_img = img.copy()
  h, w, _ = result_img.shape
  blob = cv2.dnn.blobFromImage(result_img, 1.0, (300, 300), [104, 117, 123], False, False)
  #(image, scalefactor=None, size=None, mean=None, swapRB=None, crop=None, ddepth=None)
  net.setInput(blob) # readNet 으로 만든 객체에 적용 

  # 네트워크 순방향실행 (추론) 
  detections = net.forward()

  # postprocessing
  for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > conf_threshold:
      x1 = int(detections[0, 0, i, 3] * w)
      y1 = int(detections[0, 0, i, 4] * h)
      x2 = int(detections[0, 0, i, 5] * w)
      y2 = int(detections[0, 0, i, 6] * h)

      # draw rects
      count += 1
      cv2.rectangle(result_img, (x1-20, y1-20), (x2+20, y2+20), (255, 255, 255), int(round(h/150)), cv2.LINE_AA)
      cv2.putText(result_img, '%.2f%%' % (confidence * 100.), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
      if count % 2 == 0:
        #gray = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)
        cv2.resize(result_img, (300,300))
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count / 2) + ".jpg", result_img[y1:y2,x1:x2])      

  k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
  if k == 27:
      break
  elif count >= 70: # 35장
      break

  # inference time
  tt += time.time() - start_time
  fps = frame_count / tt
  cv2.putText(result_img, 'FPS(dnn): %.2f' % (fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

  # visualize
  cv2.imshow('result', result_img)
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
import Dnn_face_training

