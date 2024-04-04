import socket


def server():
    host = socket.gethostname()
    port = 5000  # initiate port above 1024
    server_sockets = socket.socket()  # socket instance
    server_sockets.bind((host, port))  # bind host and port together
    # config how many client the server
    server_sockets.listen(2)
    conn, address = server_sockets.accept()
    print("HEY THAT IS CONNECTION FROM : " + str(address))
    while True:
        # receive the data stream , not accept data packet greater than 1024
        data = conn.recv(1024).decode()
        if not data:
            break
        print("HEY WAZZUP FROM : " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # sending data to the client


if __name__ == '__main__':
    server()
