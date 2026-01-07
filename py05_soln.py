#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--type")
    parser.add_argument("--token")
    args = parser.parse_args()
    # auth = HTTPDigestAuth('learner', 'p@ssword') # define digest auth info
    # token = requests.post('http://localhost:5000/auth/tokens', auth=auth) # get new token
    t_auth_headers = {"Authorization": f"Bearer {args.token}"} # create request header with the user-provided token
    with open(args.file, 'r') as f:
        obj = json.load(f)
        # book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."}
        requests.post(f'http://localhost:5000/api/{args.type}s', json=obj, headers=t_auth_headers) # make post request with token header
    data = requests.get(f'http://localhost:5000/api/{args.type}s')
    print(data.json())