#! /usr/bin/python3

# password_locker.py - A very insecure password locker program

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:  # if no argument was passed
    print('Usage: password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
