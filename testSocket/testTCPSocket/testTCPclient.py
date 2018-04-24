#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ss

from socket import *

HOST = 'localhost'
PORT = 5001
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    try:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
    except KeyboardInterrupt:
        print KeyboardInterrupt
        tcpCliSock.close()
    finally:
        tcpCliSock.close()

tcpCliSock.close()

