import socket

BUF_SIZE = 1024
hosts = ['127.0.0.1']
ports = [21, 22, 52, 80, 139, 443, 445, 3389, 8080]

for host in hosts:
    for port in ports:
        try:
            s = socket.socket()
            print '[+] Attempting to connect to ' + host + ':' + str(port)
            s.connect((host, port))
            s.send('xxxxxxx\n')
            banner = s.recv(BUF_SIZE)
            if banner:
                print '[+] ' + host + ':' + str(port) + ' open:\n' + banner
        except socket.error, e:
            pass
        finally:
            s.close()