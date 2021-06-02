#!/usr/bin/env python
# coding: utf8
import socket
import datetime

def _main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 9999))
        s.listen()
        print('Le serveur est en écoute')
        conn, addr = s.accept()
        with conn:
            print('Connexion de ', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(f"Données reçu à {datetime.datetime.now()} : {data}".encode())

if __name__ == '__main__':
    _main()
