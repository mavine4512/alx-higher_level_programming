#!/usr/bin/python3
'''function that creates an Object from
a “JSON file”
'''
import json


def load_from_json_file(filename):
    """Creates a python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
