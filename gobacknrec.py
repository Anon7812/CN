import socket
import time
server_address = ('localhost', 4345)
window_size = 4
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packets = ["Packet " + str(i) for i in range(10)]
next_seq_num = 0
base=0
while base<10:
    for i in range(next_seq_num, min(next_seq_num + window_size, len(packets))):
        sender_socket.sendto(packets[i].encode(), server_address)
        print(f"Sent: {packets[i]}")
        time.sleep(1)
    sender_socket.settimeout(2)
    for j in range(window_size):
        try:
            ack, _ = sender_socket.recvfrom(1024)
            ack_num = int(ack.decode())
            print(f"Received ACK: {ack_num}")
            if next_seq_num == ack_num:
                next_seq_num+=1
        except socket.timeout:
            print("Timeout: No ACK received. Resending window.")
            break
    base=next_seq_num
sender_socket.close()