#!/usr/bin/env python
# coding: utf8

import requests

r = requests.get("https://api.chucknorris.io/jokes/random")
print(r.status_code)
print(r.text)