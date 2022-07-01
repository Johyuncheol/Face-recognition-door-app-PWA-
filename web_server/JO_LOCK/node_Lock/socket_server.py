from socket import * # 소켓 모듈
from time import * 
import threading # 스레드를 
import sys


host = '192.168.137.1'
if not host:
    host = '192.168.137.1'
port = 2000


HOST = host
PORT = port
ADDR = (HOST, PORT)
BUFSIZ = 1024


def send(sock): # 메세지를 보낼 함수
    
        option=sys.argv[1]
        #sendData = input('>> ')
        sendData ='%s' % option
        #if not sendData:
         #   break
        sock.send(bytes(sendData, 'utf-8'))

        
        
def receive(sock): # 메세지를 받을 함수
    while True:
        recvData = sock.recv(BUFSIZ)
        print(recvData.decode())


        if recvData.decode() == "open_check":
            import FCM
            FCM.push(0)
            sys.exit(0)


        if recvData.decode() == "train_check":
            import FCM
            FCM.push(1)
            sys.exit(0)





cliSock = socket(AF_INET, SOCK_STREAM) # 클라이언트 소켓 생성
cliSock.connect(ADDR) # 주소로 소켓 연결

print('Connected..')

sender = threading.Thread(target=send, args=(cliSock,)) # send 함수 스레드 생성
receiver = threading.Thread(target=receive, args=(cliSock,)) # recv 함수 스레드 생성

sender.start() # send함수 스레드 활성화
receiver.start() # recv함수 스레드 활성화