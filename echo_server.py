import socket
import sys



data = {}

def set(key, value):
    data[key] = value

def get(key):
    return data[key]

def delete(key):
    del data[key]







def run_server():
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
                operation = connection.recv(16) #RECV 16 BUTES AT A TIME
                string_operation = operation.decode('utf-8')
                print(f"received: {string_operation} of type: {type(string_operation)}")
                if operation: #instead of sending data back now, we are performing operations
                    command, key, value = 0,1,2
                    operands = string_operation.split(" ")
                    response = "I don't understand that command"
                    if operands[command] == "get":
                        response = get(operands[key])
                    elif operands[command] == "set":
                        set(operands[key], operands[value])
                        response = f"{operands[key]} set to {operands[value]}"
                    elif operands[command] == "delete":
                        response = f"key {operands[key]} deleted"
                        delete(operands[key])
                    elif operands[command] == "show":
                        response = str(data)
                    else:
                        print("None of the conditions hit")
                    connection.sendall(response.encode('utf-8'))
                else:
                    print(f"no more data from {client_address}")
                    break
        finally:
            connection.close()
run_server()