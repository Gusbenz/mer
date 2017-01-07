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
headers = {'Authorization': 'token %s' % token}

# replace with class for session handling?
# http://stackoverflow.com/questions/17622439/how-to-use-github-api-token-in-python-for-requesting
# ##
class User(object):
  def __init__(self, username, token):
    self.username = username
    self.token = token

class GitHub(object):
  def __init__(self, arg):
    self.arg = arg
    self.session = requests.Session()
    req = self.session.get(base_url + 'user')
    try:
      self.session.headers['Authorization'] = 'token %s' % arg.token
      print(colored.green('You are authenticated ✔︎'))
    except AttributeError:
      print(colored.red('You are not authenticated ✔︎'))

  def get_user():
    try:
      magic_num = random.randint(1, 10987)
      u = self.session.get(base_url + 'users?since=' +
                       str(magic_num))
      users = u.json()
      user = users[0]['login']
      return user
    except KeyError:
      error = users['message']
      return colored.red('OH SHIT: %s' % error)

  def get_commit(self, user):
    user = get_user()

    # get the repo based on user
    r = self.session.get(base_url + 'users/' +
                     user + '/repos')
    repos = r.json()
    repo = repos[0]['name']

    # get the commit based on repo
    c = self.session.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits')
    commits = c.json()
    commit = commits[0]['sha']

    # get the commit message based on the sha of commit
    m = self.session.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits/' + str(commit))
    messages = m.json()
    message = messages['commit']['message']

    print(message)

def get_user():
  try:
    magic_num = random.randint(1, 10987)
    u = requests.get(base_url + 'users?since=' +
                     str(magic_num), headers=headers)
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
                   user + '/repos', headers=headers)
  repos = r.json()
  repo = repos[0]['name']

  # get the commit based on repo
  c = requests.get(base_url + 'repos/' +
                   user + '/' + repo + '/commits', headers=headers)
  commits = c.json()
  commit = commits[0]['sha']

  # get the commit message based on the sha of commit
  m = requests.get(base_url + 'repos/' +
                   user + '/' + repo + '/commits/' + str(commit), headers=headers)
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
      player = User('Gusbenz', token)
      game = GitHub(player)
    except:
      raise
  if args.commit:
    try:
      game.get_commit()
    except KeyError:
      print(get_user())
    except IndexError:
      print(colored.red('Random IndexError'))
