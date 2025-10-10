import socket


users_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
users_client_socket.connect(server_address)

message = "Привет, сервер!"
users_client_socket.send(message.encode())

response = b""
while True:
    chunk = users_client_socket.recv(1024)
    if not chunk:
        break
    response += chunk

print(response.decode())

users_client_socket.close()