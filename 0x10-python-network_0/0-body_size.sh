#!/bin/bash
# A request to an URL with curl,which display the size of the body of the response
curl -s "$1" | wc -c
