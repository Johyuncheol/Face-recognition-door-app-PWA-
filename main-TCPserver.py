import socket, threading

host = '192.168.137.1'
port = 2000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓생성
server.bind((host, port))
server.listen() #클라이언트접속대기하는 

clients = [] #접속클라이언트들


# 서버가 받은 메시지를 클라이언트 전체에 보내기
def broadcast(message):
    for client in clients:
        client.send(message)
        


def handle(client):
    while True:
        try:
            # 클라이언트로부터 타당한 메시지를 받았는지 확인(데이터읽기)
            message = client.recv(1024)

            # 브로드캐스트 함수 동작
            broadcast(message)

        except:
            # 클라이언트가 나갔으면 알림
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


# 멀티 클라이언트를 받는 메서드
def receive():
        while True:
            client, address = server.accept() # accept 함수에서 대기하다가 새 소캣리턴
            print("Connected with {}".format(str(address)))
            clients.append(client) # 클라이언트 삽입
            client.send('Connected to server!'.encode('ascii'))
            thread = threading.Thread(target=handle, args=(client,))# 스래드 생성 handle 실행 파라미터 client
            thread.start()


receive()