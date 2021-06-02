#!/usr/bin/env python
# coding: utf8

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Classe de gestion des connexions
    Instanciée à chaque connexion d'un client
    """

    def handle(self):
        # self.request est la connexion TCP du client
        self.data = self.request.recv(1024).strip()
        print(f"réception de {self.data} de {self.client_address[0]}")
        
        # retourne la chaine envoyée tout en majuscule
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # création du serveur en écoute sur le port 9999  sur toutes les interfaces
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # le serveur tourne en continue en attente de connexion
        server.serve_forever()

