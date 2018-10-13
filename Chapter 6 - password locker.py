##! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7494943KDDMDkdkdjdkdjkABE4848',
             'blog': 'dsjsdjkkjds984329iDKDKADMdnjdsajasfdhsa',
             'luggage': '321123'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       #first command line arg

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account + '.')