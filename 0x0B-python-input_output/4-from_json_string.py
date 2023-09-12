#!/usr/bin/python3
'''function that returns an object (Python data structure)
represented by a JSON string
'''
from json import JSONDecoder


def from_json_string(my_str):
    return JSONDecoder().decode(my_str)
