#!/usr/bin/env python
# -*- coding: latin-1 -*-

__doc__ = \
    """
Meaningless Experiment Realized

"""

import sys
import os
import os.path
import argparse
import random
import requests
from clint.textui import colored

user_name = 'Gusbenz'
base_url = 'https://api.github.com/'
token = os.environ.get('GITHUB_API_KEY')


def get_auth():
  authenticated = False
  a = requests.get(base_url + 'user',
                     headers={'Authorization': 'token %s' % token})
  auth = a.json()
  print(a.status_code)
  if a.status_code == 200:
    authenticated = True
    return authenticated
  else:
    authenticated = False
    return authenticated


def check_auth(authenticated):
  authenticated = authenticated()
  if authenticated is True:
    print(colored.green('You are authenticated ✔︎'))
  elif authenticated is False:
    print(colored.red('You are are authenticated ✘'))


def get_user():
  try:
    magic_num = random.randint(1, 10987)
    u = requests.get(base_url + 'users?since=' +
                     str(magic_num), headers={user_name: token})
    users = u.json()
    user = users[0]['login']
    return user
  except KeyError:
    error = users['message']
    return colored.red('OH SHIT: %s' % error)


def get_commit(user):
  user = user()
  # get the repo based on user
  r = requests.get(base_url + 'users/' +
                   user + '/repos', headers={user_name: token})
  repos = r.json()
  repo = repos[0]['name']

  # get the commit based on repo
  c = requests.get(base_url + 'repos/' +
                   user + '/' + repo + '/commits', headers={user_name: token})
  commits = c.json()
  commit = commits[0]['sha']

  # get the commit message based on the sha of commit
  m = requests.get(base_url + 'repos/' +
                   user + '/' + repo + '/commits/' + str(commit), headers={user_name: token})
  messages = m.json()
  message = messages['commit']['message']

  print(message)

#--CLI--#

cli = argparse.ArgumentParser(description=__doc__)

cli.add_argument('-c', '--commit',
                 action='store_true',
                 help='grab a random GitHub commit')

cli.add_argument('-a', '--authenticate',
                 action='store_true',
                 help='authentication for GitHub')

if __name__ == '__main__':
  args = cli.parse_args()
  if args.authenticate:
    try:
      get_auth()
      check_auth(get_auth)
    except:
      raise
  if args.commit:
    try:
      get_user()
      get_commit(get_user)
    except KeyError:
      print(get_user())
  else:
    print('Show me the money! \n Seriosuly...use the --commit flag.')
