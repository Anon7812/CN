import socket



def receiver():

    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    receiver_address = ('127.0.0.1', 8086)

    receiver_socket.bind(receiver_address)



    expected_frame_number = 0



    while True:

        data, sender_address = receiver_socket.recvfrom(1024)

        frame_number = data.decode()

        print(f"Received: {frame_number}")



        if frame_number == f"Frame {expected_frame_number}":

            ack = f"ACK {expected_frame_number}".encode()

            receiver_socket.sendto(ack, sender_address)

            print(f"Sent ACK {expected_frame_number}")

            expected_frame_number += 1



if __name__ == "__main__":

    receiver()

    #Not correct using it only in emergency