#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

def print_count(c):
    while c > 0 :
        print 'count = %d' % c
        c -= 1
        time.sleep(1)

def main():
    t = threading.Thread(target = print_count, args = (5,))
    t.start()
    t.join()

if __name__ == '__main__':
    main()
