from random import randint


def main():
    digit_random = randint(1, 11)
    while int(input('Enter digit ')) != digit_random:
        print('Failed, try again ')
    print('Nice, you win')


if __name__ == '__main__':
    main()
