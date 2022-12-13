from random import *
print('Welcome to the number game')
border_max = int(input('Enter the maximum number limit in: '))
number_rand = randint(1, border_max)
flag = 0
def is_valid(_):
    if _.isdigit() and 1 <= int(_) <= border_max:
        return True
    else:
        return False
while True:
    number_user = input('Enter number from 1 to 100: ')
    if is_valid(number_user):
        flag += 1
        number_user = int(number_user)
        if number_user < number_rand:
            print('Your number is less than expected, please try again')
        elif number_user > number_rand:
            print('Your number is higher than expected, please try again')
        elif number_user == number_rand:
            print('You guessed it, congratulations!')
            print('Number of attempts', ':', flag)
            break
    else:
        print('Maybe still enter an integer from 1 to ', border_max, '?')
print('Thanks for playing the number guessing game. See you later...')
repeat = input("Do you want to play again? If yes enter 'y', if no enter 'n': ")
if repeat == 'y':
    while True:
        number_user = input('Enter number from 1 to 100: ')
        flag = 0
        if is_valid(number_user):
            flag += 1
            number_user = int(number_user)
            if number_user < number_rand:
                print('Your number is less than expected, please try again')
            elif number_user > number_rand:
                print('Your number is higher than expected, please try again')
            elif number_user == number_rand:
                print('You guessed it, congratulations!')
                print('Number of attempts', ':', flag)
                break
        else:
            print('Or maybe still enter an integer from 1 to 100?')
    print('Thanks for playing the number guessing game. See you later...')

