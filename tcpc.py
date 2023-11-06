import socket
host = '127.0.0.1'
port = 8085
cl = socket.socket()
cl.connect((host,port))
filename = input("Enter the filename to be shared: ")
fi = open(filename, "r")
data = fi.read()
cl.send(data.encode())
print("File sent successfully")
fi.close()
cl.close()