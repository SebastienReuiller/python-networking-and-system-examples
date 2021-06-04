#!/usr/bin/env python
# coding: utf8

import argparse
import subprocess
import re
import xmltodict
#import json


def _main(target):
    print("Affiche la liste des ports ouverts")

    cmd_nmap = f"nmap -oX - -p20-30 {target}"
    output = subprocess.check_output(cmd_nmap.split(" "), universal_newlines=True)

    reponse_json = xmltodict.parse(output)
    #print(json.dumps(reponse_json, indent=4, sort_keys=True))

    
    open_ports = []
    for port in reponse_json['nmaprun']['host']['ports']['port'] :
        if port['state']['@state'] == 'open' :
            open_ports.append(port['@portid'])

    print(f"Les ports ouverts sont : {', '.join(open_ports)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target',
                        dest='target',
                        help="Adresse IP cible",
                        required=True
                        )

    args = parser.parse_args()

    _main(args.target)