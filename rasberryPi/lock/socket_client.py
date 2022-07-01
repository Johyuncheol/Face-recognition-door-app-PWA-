#Python3 FullDuplexClient

from socket import *
from time import *
import threading
import subprocess
import pyrebase 
import sys
import importlib
import RPi.GPIO as GPIO
import time

#-----------------------firebase 
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
#-----------------------

host = '192.168.137.1'

port = 2000


HOST = host
PORT = port
ADDR = (HOST, PORT)
BUFSIZ = 1024


def send(sock): # 메세지를 보내는 함수
    while True:
        sendData = input('>> ')
        sock.send(bytes('%s' % (sendData), 'utf-8'))
        
        #sock.send(bytes('[%s] 상대방: %s' % (ctime(), sendData), 'utf-8'))

def receive(sock): #메세지를 받는 함수
    while True:
        recvData = sock.recv(BUFSIZ)
        print(recvData.decode())
        

        #메세지에 대한 처리 
        if recvData.decode() == "open":
            #도어락오픈
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(12, GPIO.OUT)
            GPIO.output(12, False)
            time.sleep(1)
            GPIO.output(12, True)
            
            sock.send(bytes('%s' % 'open_check', 'utf-8'))
            db.child("도어락").child('상태').set('close')
            db.child("도어락").child('문열림알림').set('on')
            db.child("도어락").child('문열림알림').set('off')

            

        if recvData.decode() == "train":
            #import dnn_real
            #importlib.reload(dnn_real)
            storage = firebase.storage()
            storage.child('trainer.yml').download('/home/pi/lock/trainer/trainer.yml')
            sock.send(bytes('%s' % 'train_check', 'utf-8'))
            db.child("도어락").child('얼굴학습').set('off')
            db.child("도어락").child('파일다운').set('off')
         
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(12, GPIO.OUT)

            for i in range(2):
                GPIO.output(12, False)
                time.sleep(0.05)
                GPIO.output(12, True)
                time.sleep(1)
            
            

cliSock = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성
cliSock.connect(ADDR) # 주소로 소켓 연결

print('Connected..')

sender = threading.Thread(target=send, args=(cliSock,)) # send 함수 스레드 생성
receiver = threading.Thread(target=receive, args=(cliSock,)) # recv 함수 스레드 생성

sender.start() # send함수 스레드 활성화
receiver.start() # recv함수 스레드 활성화
