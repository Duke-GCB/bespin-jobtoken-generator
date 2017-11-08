#!/usr/bin/env python3

import requests
import sys
import json

API_PATH = '/admin/job-tokens/'

def post_codes(url, token, codes):
    for code in codes:
        headers = {'Authorization': 'Token {}'.format(token), 'Content-Type': 'application/json'}
        payload = make_payload(code)
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            r.raise_for_status()
        except requests.HTTPError as e:
            print('Unable to post: {}'.format(r.text))

def make_payload(code):
    return dict(token=code)

def load_codes(filename):
    with open(filename, 'r') as f:
        codes = f.read().splitlines()
    return codes

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {} <codes.txt> <bespin api root> <auth token>'.format(sys.argv[0]))
        exit(-1)
    filename, api_root, token = sys.argv[1:]
    codes = load_codes(filename)
    url = '{}{}'.format(api_root, API_PATH)
    post_codes(url, token, codes)
