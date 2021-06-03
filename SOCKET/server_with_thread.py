#!/usr/bin/env python3
# coding: utf8

import socket
import _thread
import argparse

def handle_client_cnx(cnx, addr):
    with cnx:
        print('Connexion de ', addr)
        while True:
            # reception et affichage des données du client
            data = cnx.recv(1024)
            if not data: break

            print(f"serveur reçois de {addr} : {data.decode()}")


def _main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args.bind, args.port))
        s.listen()
        print(f"Le serveur est en écoute sur {args.bind}:{args.port}")
        while True:
            print('Attente de connexion')
            conn, addr = s.accept()

            _thread.start_new_thread(handle_client_cnx, (conn, addr))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind-address',
                        dest='bind',
                        default='0.0.0.0',
                        help="Adresse IP d'écoute"
                        )
    parser.add_argument('-p', '--port',
                        dest='port',
                        help="Port d'écoute",
                        type=int,
                        default=9999
                        )

    args = parser.parse_args()

    _main(args)