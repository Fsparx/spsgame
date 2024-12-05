import socket
from _thread import *
import queue
import time
server="192.168.1.4"
port=5555
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
que = queue.Queue()
try:
    s.bind((server,port))
except socket.error as e:
    print(e)
s.listen(2)
reply={1:"",2:""}
def threaded_client(conn,count):
    conn.send(str.encode(f"Connected Player{count}"))
    if count==2:
        que.put("Start")
        conn.send(str.encode("Startigg"))
        conn.send(str.encode("Connected"))
    if count==1:
        conn.send(str.encode("Waiting for second player"))
        message=que.get()
        print(f"{message}")
        conn.send(str.encode("Connected"))
    while True:
        try:
            data=conn.recv(2048).decode()
            if not data:
                print("Disconnected1")
                break
            if count==1:
                reply[2]=data
            else:
                reply[1]=data
            while (reply[1]=="" or reply[2]==""):
                time.sleep(1)
            if (not reply[1]=="" or not reply[2]==""):
                conn.send(str.encode(reply[count]))
                time.sleep(2)
                reply[1]=""
                reply[2]=""
        except:
            pass
    conn.close()
count=0
while True:
    conn,addr=s.accept()
    print("Connected to:",addr)
    count+=1
    start_new_thread(threaded_client,(conn,count))

