# Face-recognition-door-app-PWA-

### 스마트폰제어 얼굴인식 도어락

### 개발 환경
<li>H/W : Raspberry Pi 4B, Raspberry</li> 
<li>WebCam: logitech C270 webcam</li>
<li>Galaxy tab s6 lite , iphone xs</li>
<li>O/S : Raspbian</li>
<li>IDE : visual studio code, android studio</li>

### 주요기능
<li>react를 이용하여 web app 의 형태 구현 및 firebase realtime database, storage 연동, proxy 설정을 통한 node.js 웹서버와 통신</li>
<li>node.js 웹서버에서 view를 이전 react로 적용 및 firebase의 data 변경에 따른 요청 및 응답 , push 알림 구현</li>
<li>mulit thread tcp/ip 통신을 통해 웹서버와 rasberrypi간 데이터 통신 구축 (학습된 얼굴에 대한 데이터가 전송)</li>
<li>dnn 얼굴탐지 모델사용 얼굴탐지 및 LBP 알고리즘에 의한 학습구현</li>
<li>LBP 알고리즘에 의한 학습시 이미지의 조명요소 영향을 줄이기 위해 homomorphic filter 구현 및 적용</li>
<li>시도자 실시간 확인기능</li>


![image](https://user-images.githubusercontent.com/51200912/176946167-504c4264-070a-43b2-b5ff-57a47f3a6f37.png)
![image](https://user-images.githubusercontent.com/51200912/176946188-0edb6324-aebc-4b85-9487-ec15f31d65e0.png)
![image](https://user-images.githubusercontent.com/51200912/176946208-5c5a6f1c-d1e3-4758-8bce-06044147a0ce.png)
![image](https://user-images.githubusercontent.com/51200912/176946229-59c89e6d-fd7e-48f4-83a5-8741aea86127.png)



### 구조
![image](https://user-images.githubusercontent.com/51200912/176945961-b02434a6-f446-45d4-8017-645d52b320b3.png)


