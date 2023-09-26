import socket
from _thread import *
import sys

server = "127.0.0.1"

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for connection")

masgs = ["0","1"]
idcont = 0
def thread_client(conn, idcont):
    reply = ""
    print(idcont)
    try:
        conn.send(str.encode(masgs[idcont]))
    except:
        pass
    
    while 1:
       
        try:
            data = conn.recv(2048).decode()
            masgs[idcont] = data
            if not data:
                print("Disconnected")
                break

            else:
                if data == "client_out":
                    if len(idcont):
                        idcont -= 1
                if data == "watting":
                    masgs[idcont]= "watting"
                if idcont == 0:
                    reply = masgs[1]
                else:
                    reply = masgs[0]
                
                print("Received: ", data)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    idcont -= 1
    conn.close()

while 1:
    
    conn, addr = s.accept()

    print("connected to:", addr)


    start_new_thread(thread_client, (conn,idcont))
    idcont += 1
