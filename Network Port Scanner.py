import socket
from datetime import datetime

target = input("Enter target IP address: ")

print("-" * 50)
print("       NETWORK PORT SCANNER")
print("-" * 50)

print("Target IP:", target)
print("Scanning started at:", datetime.now())

try:
    for port in range(1, 1025):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: OPEN")

        s.close()

    print("\nScanning completed!")

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Could not connect to the server.")
