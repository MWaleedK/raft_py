import socket
import sys

server_address = ('localhost', 10000)
print(f"Starting server on {server_address[0]}, port: {server_address[1]}")

sock = socket.socket()

sock.bind(server_address) #bind the server to the (ip, socket)

sock.listen(1)# listen for connection(s) from client(s)

while True:
    print("Waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print(f"Connection from Client: {client_address}")
        while True:
            data = connection.recv(16) #RECV 16 BUTES AT A TIME
            print(f"received: {data}")
            if data:
                print("Sending back data to client")
                connection.sendall(data)
            else:
                print(f"no more data from {client_address}")
                break
    finally:
        connection.close()
