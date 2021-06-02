# Python et le réseau



[TOC]

## Les sockets

### Avantages

Temps réel, bi-directionnel, paquets plus petit que le HTTP et donc les appels sont plus rapides.

### Cas d'usages

- surveillance / "health check" pour un répartiteur de charge
- simuler des échanges / honeypot
- diffuser de l'information en temps réel vers plusieurs machines

### Les modes de connexion

**Mode datagramme**

- Envois de paquets UDP
- pas  de connexion entre les parties
- pas de fiabilité (paquets perdus, paquets dans le désordre)
- multicast possible

**Mode connecté**

- connexion établi en TCP
- transmission fiables
- canal bidirectionnel

### Implémentation en Python

Exemple simple TCP (à retrouver dans SOCKET)

`server.py` :

```python
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

```



`client.py` :

```python
import socket

def _main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 9999))
        s.sendall(b'Hello !!')
        data = s.recv(1024)

    print(f'Données reçu : {data.decode()}')

if __name__ == '__main__':
    _main()

```

Que se passe t-il ?

Exemple avec `socketserver` dans `SOCKETSERVER`.



### Ressources

https://docs.python.org/3/library/socket.html

https://docs.python.org/3/library/socketserver.html



### Exercices

**Exercice Client << Serveur** 

Créer un serveur de connexion et un client. Le premier client à se connecter devient "principal" et les suivants "secondaire". Si le premier se déconnecte, le client suivant reçoit "principal".

Constater la connexion établie avec la commande netstat :

```bash
netstat -an
```

**Exercice Client >> Serveur ** :

Créer un programme Python client qui transmet toutes les modifications  d'un répertoire à un serveur. Le script client doit être lancé sur plusieurs machines contrairement au serveur qui doit être lancé qu'une fois.

**Astuce** : le module Python `inotify` permet de détecter des changements sur un répertoire.

```python
import inotify.adapters

def _main():
    i = inotify.adapters.InotifyTree('/tmp/watching')

    for event in i.event_gen():
        if event is not None:
            (header, type_names, watch_path, filename) = event

            print(f"modification {type_names} sur {filename}")

            if 'IN_CREATE' in type_names:
               print("c'est une création") 

if __name__ == '__main__':
    _main()
```



## Appeler un service HTTP

Les API REST sont partout et offre des posssibilités infinis (hook, récupération d'info, de stats).

```python
import requests

r = requests.get("https://api.chucknorris.io/jokes/random")
print(r.status_code)
print(r.text)
```

**Exercice**

Utiliser le service https://ifconfig.me/ pour récupérer l'IP publique utilisée (à mettre dans une variable et à afficher).



## Créer un script Python avec des paramètres

Comme les commandes systèmes, il est possible de passer des paramètres à un script.

En Python, le module `argparse` (https://pypi.org/project/argparse/) simplifie le travail et permet de déclarer les paramètres attendus, exemple `test_arg.py`:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first', help="Le premier argument")

args = parser.parse_args()
print(args.first)
```

Tester :


```bash
$ python test_arg.py --help
```

Puis :


```bash
$ python test_arg.py "la première valeur"
```



**Exercice** :

Créer un script avec deux paramètres, un entier nommé "repete" (par défaut à 2) et une chaine de caractères nommé "lachaine" (obligatoire). Le script affiche "repete" fois "lachaine". 



## Éxécuter une commande

Utiliser des commandes qui rendent la main

Vérifier si les commandes en question n'ont pas une sortie "facile" à interpréter par un programme (json, clé valeur etc..)

Avec os.system :
```python
import os
os.system("systemctl restart apache2")
```

Avec Popen :
```python
from subprocess import PIPE, Popen

p = Popen("ls", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
out = p.stdout.read().decode('utf-8')
err = p.stderr.read().decode('utf-8')

print(f"Sortie standard : {out}")
if p.returncode != 0:
    print(f"Sortie d'erreur : {err}")
```

Directement avec subprocess :

```python
import subprocess

output = subprocess.check_output(["systemctl", "show", service_name]
```

**Exercice** : 

À l'aide de la commande NMAP, créer une liste des ports ouverts d'une machine




## Éxécuter une commande distante

Le module Paramiko permet d'éxécuter des commandes sur une machine distante via SSH

```python
import paramiko

ssh_cnx = paramiko.SSHClient()

# ajout automatique aux serveurs connus
ssh_cnx.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_cnx.connect(hostname=SERVER, port=PORT, username=USER, key_filename=KEY_PATH)
    
ssh_stdin, ssh_stdout, ssh_stderr = ssh_cnx.exec_command('ls /tmp')
  
print(f"output : {ssh_stdout.read()}")
```



**Exercice** :

En reprenant la commande NMAP, vérifier que la liste de ports ouverts d'une machine cible est bien la même en se connectant sur plusieurs machines 



## Analyser un script de la communauté

La communauté Python est vaste et très généreuse.

- vérifier qu'il n'y a pas déjà un programme / script existant
- vérifier l'existante de modules (https://pypi.org/)
- analyser le contenu avec de l'intégrer



Exercice : analyser le script suivant et expliquer ce qu'il fait :

https://github.com/SebastienReuiller/teleinfo-linky-with-raspberry/blob/master/teleinfo.py



## Ressources

https://docs.python.org

https://pypi.org/

https://quickref.me/python

