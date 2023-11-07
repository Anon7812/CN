import random
import time

def simulate_network_delay():
    return random.randint(1, 3)


def sender(frame):
    print(f"Sender: Sending frame {frame}")
    time.sleep(simulate_network_delay())  # Simulate network delay
    return frame


def receiver(expected_frame, frames_to_send):
    time.sleep(simulate_network_delay())  # Simulate network delay
    received_frame = expected_frame if random.random() < 0.9 else None  # Simulate packet loss
    if received_frame is not None:
        print(f"Receiver: Received frame {received_frame}")
    else:
        print(f"Receiver: Frame {expected_frame} not received")
    return received_frame


def main():
    frames_to_send = 5
    frame_expected = 0
    sent_frame = sender(0)  # Store the return value of sender
    while frame_expected < frames_to_send:
        ack_received = receiver(frame_expected, frames_to_send)
        if ack_received == frame_expected:
            frame_expected += 1
            sent_frame = sender(frame_expected)  # Store the return value of sender
        else:
            print("Sender: Timeout, resending frame", frame_expected)
    print(f"Receiver: Received frame {frames_to_send}")

if __name__ == "__main__":
    main()