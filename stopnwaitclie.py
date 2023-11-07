import socket
import time
import random  # Import the random module

def sender():
    loss_prob = 0.2
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('127.0.0.1', 8086)
    frame_number = 0
    n = int(input("Enter the number of frames to send: "))

    # Define receiver_address and frame_number outside the loop
    for i in range(n):
        frame = f"Frame {frame_number}".encode()
        if loss_prob < random.random():  # Check for frame loss

            sender_socket.sendto(frame, receiver_address)
            print(f"Sent: {frame.decode()}")

            sender_socket.settimeout(2)

            try:
                ack, _ = sender_socket.recvfrom(1024)
                if ack.decode() == f"ACK {frame_number}":
                    print(f"Received ACK {frame_number}")
                    frame_number += 1
                else:
                    print(f"Invalid ACK received for frame {frame_number}. Resending...")
            except socket.timeout:
                print(f"Timeout for frame {frame_number}. Resending...")
                continue

if __name__ == "__main__":
    sender()

    #Not correct using it only in emergency