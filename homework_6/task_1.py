def is_even(number):
    if number % 2 == 0 or number == 0:
        return True
    else:
        return False


def is_even_second_func(number):
    if number % 2 == 0 or number == 0:
        result = True
    else:
        result = False
    return result


def main():
    if is_even_second_func(4):
        print('is a double digit')
    else:
        print('is not a double digit')

    if is_even_second_func(3):
        print('is a double digit')
    else:
        print('is not a double digit')


if __name__ == '__main__':
    main()
