import socket


def users_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)


    server_socket.listen(10)
    print("Сервер запущен и ждет подключений ...")

    all_data = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode().strip()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
            all_data.append(data)

            history = "\n".join(all_data)
            client_socket.send(history.encode())

        client_socket.close()


if __name__ == '__main__':
    users_server()