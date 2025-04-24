from pyfiglet import figlet_format
from usb_connection import establish_usb_connection
from diagnostics import run_diagnostics
from ai_algorithms import initialize_algorithms
from camera_module import initialize_camera
import time, os, random, shutil

def print_banner():
    print(figlet_format("System Configuration", font="slant"))
    print('\a')  # Beep on banner show
    time.sleep(1)

def matrix_rain(lines=10, duration=2):
    width = shutil.get_terminal_size().columns
    charset = "0123456789ABCDEF"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ''.join(random.choice(charset + " ") for _ in range(width))
        print('\033[92m' + line + '\033[0m')  # Green text
        time.sleep(0.05)

def main():
    print_banner()
    print("System initializing...\n")
    time.sleep(1)

    establish_usb_connection()
    run_diagnostics()

    print("Initializing Neural Core...\n")
    matrix_rain(duration=2)
    
    initialize_algorithms()
    initialize_camera()

    print(">> All systems are green. AI Framework is online.")
    print(">> System setup complete. Ready for operation.")

if __name__ == "__main__":
    main()
