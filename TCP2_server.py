#! /usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'Creating Error:', e
    sys.exit()
else:
    print 'Created.'

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #地址复用

try:
    server.bind(server_addr)
except socket.error, e:
    print 'Binding Error:', e
    sys.exit()
else:
    print 'Bind.'

server.listen(5)
print 'listening.'

while True:
    client, client_addr = server.accept()
    print 'Connected by', client_addr
    while True:
        data = client.recv(BUF_SIZE)
        print data
        client.sendall(data)

client.close()
server.close()
