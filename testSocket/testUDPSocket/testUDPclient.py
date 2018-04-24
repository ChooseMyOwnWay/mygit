#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ss

from socket import *

HOST = 'localhost'
PORT = 5001
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)

    try:
        data, ADDR =udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print data
    except KeyboardInterrupt:
        print KeyboardInterrupt
        udpCliSock.close()
    finally:
        udpCliSock.close()

udpCliSock.close()
