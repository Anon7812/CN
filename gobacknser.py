import socket
import random
server_address = ('localhost', 4345)
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind(server_address)
while True:
    data, client_address = receiver_socket.recvfrom(1024)
    packet = data.decode()
    packet_number = int(packet.split()[1])
    if random.random() < 0.2:
        print(f"Received: {packet}, Acknowledgment not sent for packet {packet_number}")
    else:
        receiver_socket.sendto(str(packet_number).encode(), client_address)
        print(f"Received: {packet}, Sent ACK: {packet_number}")
receiver_socket.close()
