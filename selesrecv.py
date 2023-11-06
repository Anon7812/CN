import socket
import time
sender_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('localhost',4445)
sequence_numbers = list(range(20))
packets = [str(i) for i in sequence_numbers]
base = 0
window_size =4
next_seq_num = 0
count=0
buffer = [False] * len(packets)
while base < len(packets):
    count=0
    for i in range (next_seq_num,min(next_seq_num+window_size,len(packets))):
        if not buffer[i]:
            count+=1
            sender_socket.sendto(packets[i].encode(), server_address)
            print(f"Sent: {packets[i]}")
    sender_socket.settimeout(2)
    for j in range(count):
        try:
            ack, _ = sender_socket.recvfrom(1024)
            ack_num = int(ack.decode())
            print(f"Received ACK: {ack_num}")
            buffer[ack_num] = True
            while buffer[next_seq_num]:
                next_seq_num+=1
        except socket.timeout:
            print("Timeout: No ACK received. Resending unacknowledged packets in the window.")
    if count==0:
        next_seq_num+=window_size
        base=next_seq_num
sender_socket.close()
