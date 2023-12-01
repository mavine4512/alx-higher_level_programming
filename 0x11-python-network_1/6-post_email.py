#!/usr/bin/python3
"""Send a POST request to a given url with a given email.
Usage: ./6-post_email.py <URL> <email>
    - Display the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = request.post(url, data=value)
    print(r.text)
