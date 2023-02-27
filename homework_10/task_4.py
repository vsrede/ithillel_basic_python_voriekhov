from random import randint


def get_integer():
    digit = randint(1, 3)
    print('Now let\'s think ... I\'m ready')
    while True:
        answer = int(input('Enter your digit: '))
        if digit == answer:
            play_agayn = input('Nice job you winner, do you wan\'t play again? '
                               'if yes enter "y", if no enter "n": ').lower()
            if play_agayn == 'y':
                get_integer()
            else:
                break
            break


def get_str():
    digit_list = [x for x in range(1, 101)]
    digit = 0
    digit = digit_list[len(digit_list) // 2]
    while True:
        answer = input(f'Is it your number {digit}? If yes enter "y"'
                       f'if now please point your number bigger or smaller? '
                       f'If smaller enter "s", if bigger enter "b": ')
        if answer == 'y':
            print('Yes, i am winner')
            break
        elif answer == 's':
            del digit_list[digit:]
            digit = digit_list[len(digit_list) // 2]
        elif answer == 'b':
            del digit_list[:digit]
            digit = digit_list[len(digit_list) // 2]
        else:
            print('Your answer doesn\'t correct, please try again')


def main():
    while True:
        enter_game = input('Do you wan\'t play the game? Please enter "y" if yes and "n" if no: ').lower()
        if enter_game == 'y':
            start = input('you guess or me? if you enter: "i" if me print:"y": ').lower()
            if start == 'i':
                get_integer()
            elif start == 'y':
                get_str()
            else:
                print('Your answer doesn\'t correct, please try again')
        elif enter_game == 'n':
            print('Bye')
            break
        else:
            print('Your answer doesn\'t correct, please try again')


if __name__ == '__main__':
    main()
