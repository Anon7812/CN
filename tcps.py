import socket

def server():
    host = '127.0.0.1'
    port = 8085

    sock = socket.socket()
    sock.bind((host,port))
    sock.listen(3)

    connect = []
    print("Server is running...")
    conn = sock.accept()

    connect.append(conn)
    print("Connected with client")

    fno = 0
    idx = 0
    for conn in connect:
        idx += 1
        filename = "output"+str(fno)+".txt"
        fno += 1
        data = conn[0].recv(1024).decode()
        fo = open(filename,"w")
        fo.write(data)
        print("Receiving from client")
        print("Received data")
        fo.close()
        print("Data stored in file ",filename)
    for conn in connect:
        conn[0].close()


if __name__ == "__main__":
    server()