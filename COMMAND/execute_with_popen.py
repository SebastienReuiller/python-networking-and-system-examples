#!/usr/bin/env python
# coding: utf8

from subprocess import PIPE, Popen

cmd = "ls /tmdsdp"
with Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) as p:

    out = p.stdout.read().decode('utf-8')
    err = p.stderr.read().decode('utf-8')

    print(f"Sortie standard : {out}")
    if p.returncode != 0:
        print(f"Sortie d'erreur : {err}")