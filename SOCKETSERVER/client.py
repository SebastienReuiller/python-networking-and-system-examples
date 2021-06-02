#!/usr/bin/env python
# coding: utf8

import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# création de la socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # connexion au serveur
    sock.connect((HOST, PORT))

    # envoi des données au serveur
    sock.sendall(bytes(data + "\n", "utf-8"))

    # réception des données du serveur
    received = str(sock.recv(1024), "utf-8")

print("Envoyé:  {}".format(data))
print("Reçu:    {}".format(received))