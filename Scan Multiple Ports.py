import socket

target = input("Enter target IP: ")
start = int(input("Starting port: "))
end = int(input("Ending port: "))

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    if s.connect_ex((target, port)) == 0:
        print("OPEN:", port)

    s.close()

print("Scanning finished!")
