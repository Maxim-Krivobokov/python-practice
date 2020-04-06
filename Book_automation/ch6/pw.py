#! python3
#pw.py - program for unsecure password keeping


PASSWORDS = {'email': 'po4ta_po4ta_pe4kin',
             'blog': 'blogblogblog123321',
             'luggage': '12345' }

import sys, pyperclip

if len(sys.argv) < 2:
    print('You should enter an argument - name of your credential/login')
    sys.exit()

account = sys.argv[1] # first argument is the login name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' is copied to buffer.')
else:
    print('Credentials for ' + account + ' are not presented in database.')

