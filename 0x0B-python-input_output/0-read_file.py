#!/usr/bin/python3
"""Define a function"""


def read_file(filename=""):
    """Reads afile"""
    with open(filename, encoding="utf-8") as f:
        read_f = f.read()
        print(read_f, end="")
