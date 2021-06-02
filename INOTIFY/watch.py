#!/usr/bin/env python
# coding: utf8

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