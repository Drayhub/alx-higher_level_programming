#!/usr/bin/python3
"""
Read and print the content of a file
"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf8") as file:
        print(file.read())

