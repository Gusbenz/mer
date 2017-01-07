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
from requests.auth import AuthBase
from clint.textui import colored

base_url = 'https://api.github.com/'
token = os.environ.get('GITHUB_API_KEY')

# replace with class for session handling?
# http://stackoverflow.com/questions/17622439/how-to-use-github-api-token-in-python-for-requesting
# ##
class GitHub_Auth(AuthBase):
  def __init__(self, username, token):
    self.username = username
    self.token = token

  def __call__(self, r):
    r.headers['Authorization'] = 'token %s' % self.token
    return r

def get_commit(token):

    magic_num = random.randint(1, 10987)
    u = requests.get(base_url + 'users?since=' +
                      str(magic_num), auth=GitHub_Auth('Gusbenz', token))
    users = u.json()
    user = users[0]['login']

    # get the repo based on user
    r = requests.get(base_url + 'users/' +
                     user + '/repos', auth=GitHub_Auth('Gusbenz', token))
    repos = r.json()
    repo = repos[0]['name']

    # get the commit based on repo
    c = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits', auth=GitHub_Auth('Gusbenz', token))
    commits = c.json()
    commit = commits[0]['sha']

    # get the commit message based on the sha of commit
    m = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits/' + str(commit), auth=GitHub_Auth('Gusbenz', token))
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
      get_commit(token)
    except:
      raise
  if args.commit:
    try:
      game.get_commit()
    except KeyError:
      print(get_user())
    except IndexError:
      print(colored.red('Random IndexError'))
