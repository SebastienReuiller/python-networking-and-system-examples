#!/usr/bin/env python
# coding: utf8

import subprocess

def service_status_ok(service_name):
    key_value = subprocess.check_output(["systemctl", "show", service_name], universal_newlines=True).split('\n')
    json_dict = {}
    for entry in key_value:
        kv = entry.split("=", 1)
        if len(kv) == 2 and "State" in kv[0]:
            json_dict[kv[0]] = kv[1]

    return json_dict['ActiveState'] == "active" and json_dict['LoadState'] == "loaded"

def _main():
    print(f"mysql is ok : {service_status_ok('mysql')}")
    print(f"apache2 is ok : {service_status_ok('apache2')}")

if __name__ == '__main__':
    _main()