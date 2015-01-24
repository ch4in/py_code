#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'Creating Error', e
    sys.exit()
else:
    print 'Created'

client.connect(server_addr)

while True:
    data = raw_input('input:')
    if data:
        client.sendall(data)
        data = client.recv(BUF_SIZE)
        print data
    else:
        print 'Input something.'
client.close()
