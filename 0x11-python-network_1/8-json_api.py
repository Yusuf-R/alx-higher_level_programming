#!/usr/bin/python3
"""
takes letter and sends a POST req to http://0.0.0.0:5000/search_user"""
import requests
from sys import argv


if __name__ == '__main__':
    letter = {'q': argv[1][0] if len(argv) > 1 else ''}
    rv = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        response = rv.json()
        if response:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
