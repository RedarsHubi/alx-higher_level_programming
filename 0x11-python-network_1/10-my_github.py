#!/usr/bin/python3
"""script that takes GitHub credentials"""

import requests
import sys

if __name__ == "__main__":
    username = "redarshubi"
    password = ("github_pat_11A7URVVA0uRJ"
                "L2MnKiw6L_bMq87RsTLW07aBYOfHjW"
                "eHSjnUHFJIoaTNY6j3uiYpl4Q6UMCCRRjIw7mAo")
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("None")
