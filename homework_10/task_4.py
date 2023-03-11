from random import randint

game_continue = [{0: 'Okey, let\'s go'}, {1: 'Bye'}]


def get_integer(prompt=None, options=None):
    while True:
        try:
            choice_input = input(prompt)
            choice = int(choice_input)
            return choice
        except ValueError:
            print('Enter the digit 0 or 1')


def get_str(prompt):
    while True:
        value = input(prompt)
        if value:
            return value


def game(choice):
    digit_list = [x for x in range(1, 101)]
    if choice == 0:
        digit = randint(1, 100)
        answer = ''
        while digit != answer:
            answer = input('Enter you digit: ')
            if answer.isdigit():
                answer = int(answer)
                if 0 < answer < 101:
                    if answer == digit:
                        print("You win!")
                    elif answer > digit:
                        print('My digit is less')
                    elif answer < digit:
                        print('My digit is bigger')
            else:
                print('Try again, you digit must be between 1 and 100 and use only numbers')
    elif choice == 1:
        low = 1
        high = 100
        answer = ''
        while answer != 'y':
            digit = (low + high) // 2
            answer = input(f'Is it your number {digit}? If yes enter \'y\', '
                           f'if now please point your number bigger or smaller? '
                           f'If smaller enter \'s\', if bigger enter \'b\': ').lower()
            if answer == 'y':
                print('Yes, i am winner')
                break
            elif answer == 's':
                high = digit - 1
            elif answer == 'b':
                low = digit + 1
            else:
                print('Your answer doesn\'t correct, please try again')
            if high < 1 or low > 100:
                print('You are liar')
                break


def main():
    while True:
        print('Game 0 -> Guess you')
        print('Game 1 -> Guess I')
        game_choice = get_integer('Enter 0 or 1: ')

        if game_choice == 0 or game_choice == 1:
            game(game_choice)
        else:
            print('You input incorrect, please enter again')

        game_repeat = get_str('Do you wan\'t play again? Enter \'y\' or \'n\': ')
        if game_repeat != 'y':
            print('Bye')
            break


if __name__ == '__main__':
    main()

