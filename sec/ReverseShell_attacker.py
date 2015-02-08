#! /usr/bin/env python
# -*- coding:utf-8 -*-
import socket

BUF_SIZE = 2048
server_addr = ('0.0.0.0', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_addr)
s.listen(5)
print 'Listening on port 8888.'
client, client_addr = s.accept()
print 'Received connection from:', client_addr[0], client_addr[1]
while True:
    cmd = raw_input(' $ ')
    encode = bytearray(cmd)
    for i in range(len(encode)):
        encode[i] ^= 0x23
    client.send(encode)
    data = client.recv(BUF_SIZE)
    decode = bytearray(data)
    for i in range(len(decode)):
        decode[i] ^= 0x23
    print decode
client.close()
s.close()