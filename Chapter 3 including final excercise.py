#Werken met functies
#GuessGame
""" import random
low = 1
high = 20
secretNumber = random.randint(low, high)
print('The number that you have to guess is between ' + str(low) + ' and ' + str(high) + '.')

#Ask for input
for AmountGuesses in range(1, 8):
    print('Guess a number.')
    number = int(input())

    if number < secretNumber:
        print('Your guess is too low, try again.')
    elif number > secretNumber:
        print('Your number is too high, try again.')
    else:
        break #the number is correct

print('You guessed ' + str(AmountGuesses) + ' times and the result is that...')
if number == secretNumber:
    print('You guessed the secret number ' + str(secretNumber) + '!')
else:
    print('You did not guess the secret number ' + str(secretNumber) + '!') """

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    if number % 2 == 1:
        number = 3 * number + 1
        print(number)
        return number

#Collatz program
while True:
    try:
        print('Enter number:')
        returnValue = collatz(int(input()))
        while (returnValue != 1):
            returnValue = collatz(returnValue)
        else:
            print('The number is one. Goodbye!')
            break
    except ValueError:
        correct = False
        print('No integer entered, please try again by giving a correct input!')

