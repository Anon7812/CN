import socket

def client():
    host = '127.0.0.1'
    port = 8085

    sock = socket.socket()
    sock.connect((host,port))

   
    while True:
        filename = input("Enter the filename to be shared:")
        try:
            fo = open(filename,"r")
            data = fo.read()
            if not data:
                break
            sock.send(data.encode())
            fo.close()
        except IOError:
            print("File does not exist")
            break

if __name__ == "__main__":
    client()