import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#where to send data? here(ip,port):
server_address = ('localhost', 10000)
print(f"connecting to {server_address[0]}, port: {server_address[1]}")
sock.connect(server_address)

try:
    message = input("Your Message")
    print(f"sending message: {message}")
    sock.sendall(message.encode('utf-8')) #encode in utf-8 format which is bytes and sockets communicate in bytes


    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"received: {data}")
finally:
    print("Closing Socket")
    sock.close()