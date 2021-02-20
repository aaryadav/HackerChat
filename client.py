import socket
import select
from _thread import *
# import sys

server = socket.gethostname()
port = 1234
# print(server)

cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
chat_list = []

def receiver():
  try:
    while True:
      user_msg = cs.recv(2048).decode('utf-8')
      print(user_msg)
      break
  except Exception as e:
    print(e)


def sender(msg):
  if msg:
    msg = msg.encode('utf-8')
    cs.send(msg)


try:
    cs.connect((server,port))
    print("Client Connected to Server!!")
except:
    print("Something wrong here.\nDid you turn on the server?")

else:
  while True:
    usrname = input("Enter username: ")

    l= [i for i in usrname if 65<=ord(i)<=90  or 97<=ord(i)<=122]
    if not len(usrname) or len(usrname)!=len(l):
        continue
    cs.send(usrname.encode('utf-8'))
    break
  print("Start typing and hit 'Enter' key to send a message.\nType 'wiki','tempcheck' or 'ask:' followed by query to get a Wikipedia summary, temperature data or answers to general questions respectively.\nFor example 'wiki Elon Musk'")
  while True:
    start_new_thread(receiver,())
    msg = input()
    start_new_thread(sender,(msg,))

