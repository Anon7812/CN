import socket

udpcli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_add = ('127.0.0.1', 8085)

response = b"Hello good morning"
udpcli.sendto(response, server_add)

data, server = udpcli.recvfrom(1024)
print(f"Received message from {server}: {data.decode('utf-8')}")

udpcli.close()