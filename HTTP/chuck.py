#!/usr/bin/env python
# coding: utf8

import requests
import json

r = requests.get("https://api.chucknorris.io/jokes/random")

if r.status_code == 200:

    data = r.json()

    print(json.dumps(data, sort_keys=True, indent=4))

    print(data.get('id'))
    print(data.get('value'))
