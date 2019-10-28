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

n = 3 if args.numpr is None else int(args.numpr)
url = 'https://api.github.com/repos/{0}/{1}/pulls'.format(args.owner, args.repos)
r = requests.get(url, auth=(args.login, init_password))
jsondata = r.json()
# get the last n PR
if jsondata == []:
    print("There is no data about PULL REQUEST!")
else:
    getthelast3PR = jsondata[:n]
    for i in range(n):
        print("Number of PR: {0}".format(getthelast3PR[i]['number']))
        print("Title of PR: {0}".format(getthelast3PR[i]['title']))
        print("Login PR's user: {0}".format(getthelast3PR[i]['user']['login']))
        print("PR was created: {0}".format(getthelast3PR[i]['created_at']))
        print("===================================")
