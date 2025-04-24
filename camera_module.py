import time
import sys
import logging

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def print_dots_line(message, count=20, delay=0.05):
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(count):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def initialize_camera():
    print_dots_line("Scanning camera module", count=20, delay=0.04)
    logging.info("Camera module found.")
    steps = [
        "Loading camera driver",
        "Setting resolution to 1280x720",
        "Starting video feed"
    ]
    for step in steps:
        sys.stdout.write(step + ' ')
        sys.stdout.flush()
        for _ in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.3)
        print(" done.")
    print("\nCamera initialized successfully.\n")
