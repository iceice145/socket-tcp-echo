import socket
import threading

def handle_client(c,addr):
    print(addr,"connected.")
    while True:
        try:
            data = c.recv(1024)
            if not data or data.lower() == 'exit':
                break  # 无数据或exit则断开
            print(f"{addr}: {data}")
            # 回声回复 + 服务器可主动输入发送（一行实现）
            c.send(f"{data}".encode('utf-8'))
        except:
            break
    c.close()

HOST='0.0.0.0'
PORT=1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
    s.bind((HOST,PORT))
    s.listen()

    while True:
        c,addr = s.accept()

        t=threading.Thread(target=handle_client,args=(c,addr)).start()
