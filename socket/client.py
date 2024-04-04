import socket


def client():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()  # instantiation of socket
    client_socket.connect((host, port))
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()  # receive the response
        print("YOOOOOO I'AM RECEIVED SERVER FROM " + data)
        message = input("->")

    client_socket.close()  # close the  connection


if __name__ == '__main__':
    client()
