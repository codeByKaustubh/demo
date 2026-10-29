import socket

ip = input("Enter IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

for p in range(start, end + 1):
    s = socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((ip, p)) == 0:
        print(p, "OPEN", socket.getservbyport(p, "tcp") if p < 1024 else "Unknown")
    s.close()