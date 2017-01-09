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
token = os.environ.get('GITHUB_API_TOKEN')


class GitHub_Auth(AuthBase):

    def __init__(self, username, token):
        self.username = username
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'token %s' % self.token
        return r


def check_for_token():
    if 'GITHUB_API_TOKEN' in os.environ:
        print(colored.green('GITHUB_API_TOKEN is set!'))
        return True
    else:
        return False

def ask_for_login():
    global login
    login = raw_input('Enter your GitHub login: ')
    return login


def get_commit(login, token):

    magic_num = random.randint(1, 10987)
    u = requests.get(base_url + 'users?since=' +
                     str(magic_num), auth=GitHub_Auth(login, token))
    users = u.json()
    user = users[0]['login']

    # get the repo based on user
    r = requests.get(base_url + 'users/' +
                     user + '/repos', auth=GitHub_Auth(login, token))
    repos = r.json()
    repo = repos[0]['name']

    # get the commit based on repo
    c = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits', auth=GitHub_Auth(login, token))
    commits = c.json()
    commit = commits[0]['sha']

    # get the commit message based on the sha of commit
    m = requests.get(base_url + 'repos/' +
                     user + '/' + repo + '/commits/' + str(commit), auth=GitHub_Auth(login, token))
    messages = m.json()
    commiter = messages['commit']['author']['name']
    message = messages['commit']['message']

    print(colored.green('Here\'s a random commit from ' + colored.blue(commiter + ':',
                                                                       bold=True) + '\n', bold=True) + colored.white(message, bold=True))


def error():
    print(colored.red('IndexError. No repos or commits? Trying again...', bold=True))
    get_commit(login, token)
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
                ask_for_login()
                if len(login) is not 0:
                    get_commit(login, token)
                else:
                    print(colored.red('Log in, please!'))
            else:
                print(colored.red('GITHUB_API_TOKEN has not been set.'))
        except KeyError:
            print(colored.red('KeyError. No repos or commits? Trying again...', bold=True))
            get_commit(login, token)
        except IndexError:
            print(colored.red('IndexError. No repos or commits? Trying again...', bold=True))
            get_commit(login, token)
        except UnicodeEncodeError:
            print(colored.red('UnicodeEncodeError. Trying again...', bold=True))
            get_commit(login, token)
