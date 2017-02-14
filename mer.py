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
import emoji

from requests.auth import AuthBase
from clint.textui import colored

base_url = 'https://api.github.com/'
token = os.environ.get('GITHUB_API_TOKEN')


class GitHub_Auth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'token %s' % self.token
        return r


def check_for_token():
    if 'GITHUB_API_TOKEN' in os.environ:
        print(emoji.emojize(':sparkles:'))
        return True
    else:
        return False


def get_commit(token):

    magic_num = random.randint(1, 100987)
    u = requests.get(base_url + 'users?since=' +
                     str(magic_num), auth=GitHub_Auth(token))
    users = u.json()
    user = users[0]['login']

    # get the repo based on user
    r = requests.get(base_url + 'users/' +
                     user + '/repos', auth=GitHub_Auth(token))
    repos = r.json()
    repo = repos[0]['name']

    # get the commit based on repo
    c = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits', auth=GitHub_Auth(token))
    commits = c.json()
    commit = commits[0]['sha']

    # get the commit message based on the sha of commit
    m = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits/' + str(commit), auth=GitHub_Auth(token))
    messages = m.json()
    commiter = messages['commit']['author']['name']
    message = messages['commit']['message']

    print(colored.green('Here\'s a random commit from ' + colored.blue(commiter + ':',
                                                                       bold=True) + '\n', bold=True) + colored.white(message, bold=True))


#--CLI--#

cli = argparse.ArgumentParser(description=__doc__)

cli.add_argument('-c', '--commit',
                 action='store_true',
                 help='grab a random GitHub commit')


if __name__ == '__main__':
    args = cli.parse_args()
    if args.commit:
        try:
            if check_for_token() == True:
                get_commit(token)
            else:
                print(colored.red('GITHUB_API_TOKEN has not been set.'))
        except KeyError:
            print(colored.red('KeyError. Trying again...', bold=True))
            print(emoji.emojize(':dizzy_face:'))
            get_commit(token)
        except IndexError:
            print(colored.red('IndexError. Trying again...', bold=True))
            print(emoji.emojize(':dizzy_face:'))
            get_commit(token)

        except UnicodeEncodeError:
            print(colored.red('UnicodeEncodeError. Trying again...', bold=True))
            print(emoji.emojize(':dizzy_face:'))
            get_commit(token)
