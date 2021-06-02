#!/usr/bin/env python
# coding: utf8
import socket

def _main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 9999))
        s.sendall(b'Hello !!')
        data = s.recv(1024)

    print(f'Données reçu : {data.decode()}')

if __name__ == '__main__':
    _main()
