from random import randint

game_continue = {'y': True, 'n': False}
game_letters = {'y': True, 'n': False, 's': 'smaller', 'b': 'bigger'}


def get_integer(prompt=None, lower_bound=None, upper_bound=None):
    while True:
        digit = input(prompt)
        if digit.isdigit():
            digit = int(digit)
            if lower_bound <= digit <= upper_bound:
                return digit
        else:
            print('Try again, enter only digit')


def get_str(prompt=None, options=None):
    while True:
        answer = input(prompt).lower()
        if answer in options:
            return options[answer]
        else:
            print('Try again, your enter must be only one letter')


def game(choice):
    if choice == 0:
        digit_random = randint(1, 100)
        answer = 0
        while digit_random != answer:
            answer = get_integer('Enter the digit between 0 and 101: ', lower_bound=0, upper_bound=100)
            if answer == digit_random:
                print('You win!')
            elif answer < digit_random:
                print('Your digit is less')
            elif answer > digit_random:
                print('Your digit is bigger')

    elif choice == 1:
        low = 1
        high = 100
        answer = ''
        while answer != 'y':
            digit = (low + high) // 2
            answer = get_str(f'Is it your number {digit}? If yes enter \'y\', '
                             f'if now please point your number bigger or smaller? '
                             f'If smaller enter \'s\', if bigger enter \'b\': ', game_letters)
            if answer == True:
                print('Yes, i am winner')
                break
            elif answer == 'smaller':
                high = digit - 1
            elif answer == 'bigger':
                low = digit + 1


def main():
    while True:
        print('Game 0 -> Guess you')
        print('Game 1 -> Guess I')
        game(get_integer('Enter 0 or 1: ', lower_bound=0, upper_bound=1))

        if get_str('Do you wan\'t play again? Enter \'y\' or \'n\': ', game_letters):
            print('Okey, let\'s go')
        else:
            print('Bye')
            break


if __name__ == '__main__':
    main()
