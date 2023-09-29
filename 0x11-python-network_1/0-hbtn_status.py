#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", content.decode('utf-8'))
