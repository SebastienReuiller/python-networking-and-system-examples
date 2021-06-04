#!/usr/bin/env python
# coding: utf8

import subprocess
import re

def _main():
    print("Récupère le pourcentage de paquet perdu")
    output = subprocess.check_output("ping -c 3 1.1".split(" "), universal_newlines=True)

    for line in output.split('\n'):

        result = re.findall(r"([0-9]+)% packet loss", line)
        if result:
            print(f"Pourcentage : {result[0]}")

if __name__ == '__main__':
    _main()