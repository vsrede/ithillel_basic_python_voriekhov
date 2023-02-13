def is_even(number):
    return number % 2 == 0 or number == 0


def main():
    if is_even(3):
        print('is a double digit')
    else:
        print('is not a double digit')


if __name__ == '__main__':
    main()
