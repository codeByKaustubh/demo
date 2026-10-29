import socket
ip = "192.168.56.1"
for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.2)
    if s.connect_ex((ip, port)) == 0:
        print("Open Port:", port)
    s.close()