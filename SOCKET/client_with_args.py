#!/usr/bin/env python
# coding: utf8
import socket
import inotify.adapters
import argparse

def _main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((args.server, args.port))

        print(f"je suis connecté à {args.server}:{args.port} !")

        user_exit = False
        while not user_exit:


            i = inotify.adapters.InotifyTree(args.directory)

            for event in i.event_gen():
                if event is not None:

                    (header, type_names, watch_path, filename) = event

                    print(f"modification {type_names} sur {filename}")

                    if 'IN_CREATE' in type_names:
                        print("c'est une création")

                        s.sendall(f"CREATE:{filename}".encode())


                

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server-address',
                        dest='server',
                        default='127.0.0.1',
                        help="Adresse du serveur"
                        )
    parser.add_argument('-p', '--port',
                        dest='port',
                        help="Port d'écoute du serveur",
                        type=int,
                        default=9999
                        )
    parser.add_argument('-d', '--directory',
                        dest='directory',
                        help="Répertoire à surveiller",
                        type=str,
                        required=True
                        )

    args = parser.parse_args()
    _main(args)
