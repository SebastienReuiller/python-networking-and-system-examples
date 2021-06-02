#!/usr/bin/env python
# coding: utf8

import argparse

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first', help="Le premier argument")

    args = parser.parse_args()
    print(args.first)

if __name__ == '__main__':
    _main()