#!/bin/bash/env python
import requests
from getpass import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("login", help="Login name to github.com")
parser.add_argument("owner", help="Owner's name on github.com")
parser.add_argument("repos", help="Repo's name on github.com")
parser.add_argument("--numpr", help="Output number pull request")
parser.add_argument('-v', action='version', version="Program's version is 0.0.1")
args = parser.parse_args()

init_password = getpass()

n = 3 if args.numpr == None else int(args.numpr)
url = 'https://api.github.com/repos/{0}/{1}/pulls'.format(args.owner, args.repos)
r = requests.get(url, auth=(args.login, init_password))
jsondata = r.json()
# get the last n PR
if jsondata is None:
    print("There is no data about PULL REQUEST!")
else:
    getthelast3PR = jsondata[:n]
    for i in range(n):
        print(getthelast3PR[i]['number'])
        print(getthelast3PR[i]['title'])
        print(getthelast3PR[i]['user']['login'])
        print(getthelast3PR[i]['created_at'])
        print("========================")
