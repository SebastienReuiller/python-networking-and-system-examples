#!/usr/bin/env python
# coding: utf8
import requests

from bs4 import BeautifulSoup


URL = "https://www.cert.ssi.gouv.fr/"

def _main():
    # récupération du contenu de la page
    response = requests.get(URL)
    
    # parse le HTML
    html = BeautifulSoup(response.text, 'html.parser')

    # Extrait les alertes
    alerts_html = html.find_all('div', class_="cert-alert")

    # Parcours les balises alertes
    for tag_alert in  alerts_html:
        children = tag_alert.findChildren("span" , class_="item-title")
        # Parcours les balises enfants
        for child in children:
            print(child.text)

if __name__ == '__main__':
    _main()
