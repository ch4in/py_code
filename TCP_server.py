#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #地址复用
s.bind(server_addr)
s.listen(5)
while True:
    client, client_addr = s.accept()
    print 'client address:', client_addr
    while True:
        data = client.recv(BUF_SIZE)
        print data
        client.sendall(data)
s.close()
