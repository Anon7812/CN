import socket

udpser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_add = ('127.0.0.1',8085)

udpser.bind(server_add)

print(f"UDP server is listening on {server_add}")

while True:
    data, client = udpser.recvfrom(1024)
    print(f"Received message from {client}: {data.decode('utf-8')}")

    response = b"Hello hi"
    udpser.sendto(response, client)