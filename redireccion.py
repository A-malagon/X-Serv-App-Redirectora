#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Infinite HTTP Server
"""
import socket
import random
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))
mySocket.listen(5)


try:
    while True:
        numeroAleatorio = random.randint(0, 500000000)
        print 'Waiting for connections...'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 301 Movido permanente\nLocation: http://" +
                        socket.gethostname() + ":1234/" + "Hola/" +
                        str(numeroAleatorio) + "/Dame otra" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
