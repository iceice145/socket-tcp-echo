import socket
import threading
def recv_msg(s):
    # 持续读服务器消息
    while True:
        try:
            data = s.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Server: {data}")
        except:
            break
HOST='127.0.0.1'
PORT=1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=recv_msg, args=(s,), daemon=True).start()
    # 持续输入发送消息
    while True:
        msg = input()
        s.send(msg.encode('utf-8'))
        if msg.lower() == 'exit':
            break