import os
import time

def checkping(hostname):
    response = os.system(f"ping -c 1 {hostname} > /dev/null 2>&1")

    if response == 0:
        print(f"{hostname} is UP!")
    else:
        print(f"{hostname} is DOWN!")
print("starting ping monitor, type crtl+c to stop")
try:
    while True:
        checkping("google.com")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nmonitoring stopped")
