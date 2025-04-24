import time
import logging
import random

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def run_diagnostics():
    print("Running system diagnostics...\n")
    tasks = [
        "→ Checking hardware integrity",
        "→ Loading kernel modules",
        "→ Performing memory test",
        "→ Verifying firmware checksum",
        "→ Initializing thermal monitor"
    ]
    for task in tasks:
        logging.info(task)
        time.sleep(random.uniform(0.3, 0.7))
    print("\nDiagnostics completed successfully!\n")
