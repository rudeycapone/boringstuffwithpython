#Executes the programs in chapter2
""" print('What is your name?')
myName = input()
if myName == 'Ruud':
    print('Hi Ruud!')
else:
    print('Intruder detected! Get out of the system!') """

""" print('What is your name?')
myName = input()
print('Thank you! And what is your age?')
myAge = int(input())
#if statement age
if myAge > 2001:
    print('You are old enough to use the system, great!')
elif myAge < 20:
    print('Too young, you intruder!')
else:
    print('Some kind of funny kid.') """

#Excercise number 3
#Infinite while loop

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('Exiting program.')
        sys.exit()
    print('You typed ' + response + '.')


