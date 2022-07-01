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


![image](https://user-images.githubusercontent.com/51200912/176945484-2becd69c-e653-4b12-b9f2-2a38c79ac613.png)
![image](https://user-images.githubusercontent.com/51200912/176945504-046ec70b-2d28-41a2-aa1c-bbddada50a46.png)
![image](https://user-images.githubusercontent.com/51200912/176945517-1a3b146b-db1a-46c8-93c2-f2ff76553661.png)
![image](https://user-images.githubusercontent.com/51200912/176945528-b0461ce1-2427-4ca0-a330-2daf8ec6573a.png)


### 구조
![image](https://user-images.githubusercontent.com/51200912/176945904-87f369a0-3e29-47d7-a995-5fbe990a4ef8.png)


