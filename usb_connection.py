import time
import sys

def print_dots_line(message, count=30, delay=0.05):
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(count):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def establish_usb_connection():
    print_dots_line("Establishing USB connection", count=30, delay=0.04)
    print("Connection established successfully!")
    print("Baud rate: 115200\n")
    time.sleep(0.3)
