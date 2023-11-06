import socket
host = '127.0.0.1'
port = 8085
serv = socket.socket()
serv.bind((host,port))
serv.listen(3)
print("Server is running...")
conn, _ = serv.accept()
data = conn.recv(1024).decode()
filename = "output.txt"
fo = open(filename, "w")
fo.write(data)
print("File received successfully")
fo.close()