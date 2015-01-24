#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread
import time

def print_count(thread_name, delay):
    c = 0
    while c <5:
        time.sleep(delay)
        c += 1
        print '%s : %s' % (thread_name, str(c))

try:
    thread.start_new_thread(print_count, ('Thread1', 2))
    thread.start_new_thread(print_count, ('Thread2', 4))
except :
    print 'Error.'

while True: pass
