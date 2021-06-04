#!/usr/bin/env python
# coding: utf8
import argparse
import requests
from requests.exceptions import ConnectionError, MissingSchema
from json.decoder import JSONDecodeError

def _main(url):
    try:
        response = requests.get(url)

        response.json()

        print(response)

        print("fin du try catch, que si il n'y a pas d'exception dans le bloc")
    except MissingSchema:
        print("L'url n'est pas valide")
    except ConnectionError:
        print("Erreur de connexion au service")
    except JSONDecodeError:
        print("Le service nous a retourner un JSON invalide :(")
    finally:
        print("Après le try, quoi qu'il arrive")

    print("apres le bloc try catch")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        help="URL du service cible",
                        type=str,
                        required=True
                        )

    args = parser.parse_args()

    _main(args.url)
