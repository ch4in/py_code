#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, e:
    raise e
else:
    print 'Socket Created.'

try:
    server.bind(server_addr)
except socket.error, e:
    raise e
else:
    print 'Bind.'

while True:
    print 'waiting for data'
    data, client_addr = server.recvfrom(BUF_SIZE)
    print 'Connected by', client_addr
    print 'Receive data:', data
    server.sendto('Data received.', client_addr)

server.close()