#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(server_addr)
while True:
    data = raw_input('input:')
    c.sendall(data)
    data = c.recv(BUF_SIZE)
    print data
c.close()
