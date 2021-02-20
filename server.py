import socket
from _thread import *
import checker

server = socket.gethostname()
port = 1234
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind((server,port))
ss.listen()
#print(server)
print(f"Server {server} Successfully Started!!")

clients = []

def threader(clientname,usr):
  while True:
    try:
      msg = receiver(clientname)
      if msg is False:
        print(f"Connection with {usr} closed")
        clients.remove(clientname)
        print(clients)
        break
      r = checker.checker(msg)
      # print(r)
      if r is False:
        print(f"From [{usr}] : {msg}")
        broadcaster((f"[{usr}] : {msg}").encode('utf-8'),clientname)
      else:
        print(f"From [BOT] : {r}")
        broadcaster((f"[BOT] : {r}").encode('utf-8'),clientname,1)

    except:
      continue

def receiver(clientsocket):
  try:
    msg_received = clientsocket.recv(2048).decode('utf-8')

    if not len(msg_received):
      return False
    return msg_received

  except:
    return False


def broadcaster(msg,clientname="",r=""):
  for client in clients:
    if client != clientname:
      try:
        client.send(msg)
      except:
        clients.remove(client)
  if r==1:
    for client in clients:
      try:
        client.send(msg)
      except:
        clients.remove(client)


while True:
  clientsocket, address = ss.accept()
  username = receiver(clientsocket)

  if username is False:
    print("No user.")
    continue
  clients.append(clientsocket)

  print(f"Connection with {address} has been established!")
  print(f"USERNAME : {username}")
  # print(clients)
  start_new_thread(threader,(clientsocket,username))
