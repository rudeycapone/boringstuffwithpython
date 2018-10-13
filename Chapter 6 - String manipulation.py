#Chapter 6 - String Manipulation

#Catnipping
""""print('''Dear Alice,

Eve's cat has been arrested for catnipping, cat burglary, and extortion.

Sincerly,
Bob''')"""

""""print('How do you feel?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is great too.')"""

#TestProgram with numbers

""""while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Pleaes enter a valid number.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')"""

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()

