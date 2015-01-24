#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, e:
    raise e
else:
    print 'Socket Created.'

while True:
    data = raw_input('input:')
    client.sendto(data, server_addr)
    data = client.recvfrom(BUF_SIZE)[0]
    print 'Data:', data

client.close()