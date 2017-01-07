#!/usr/bin/env python

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

# userName =
base_url = 'https://api.github.com/'
token = os.environ.get('GITHUB_API_KEY')


def get_user():
  magic_num = random.randint(1, 10987)
  try:
    u = requests.get(base_url + 'users?since=' +
                   str(magic_num), headers={'Gusbenz': token})
    users = u.json()
    user = users[0]['login']
    return user
  except KeyError:
      user = users
      print(user)

def get_commit(user):
  user = user()
  ## get the repo based on user
  r = requests.get(base_url + 'users/' +
                     user + '/repos', headers={'Gusbenz': token})
  repos = r.json()
  repo = repos[0]['name']

  ## get the commit based on repo
  c = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits', headers={'Gusbenz': token})
  commits = c.json()
  commit = commits[0]['sha']

  ## get the commit message based on the sha of commit
  m = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits/' + str(commit), headers={'Gusbenz': token})
  messages = m.json()
  message = messages['commit']['message']

  print(message)

#--CLI--#

cli = argparse.ArgumentParser(description=__doc__)

cli.add_argument('-c', '--commit',
                 action='store_true',
                 help='grab a random GitHub commit')

if __name__ == '__main__':
  args = cli.parse_args()
  if args.commit:
    get_user()
    get_commit(get_user)
  else:
    print('Show me the money! \n Seriosuly...use the --commit flag.')
