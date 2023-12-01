#!/usr/bin/python3
"""Display the X-Request_Id header variable of a reuest to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.header.get("X-Request_Id"))
