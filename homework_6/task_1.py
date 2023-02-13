def is_even(number):
    if number % 2 == 0 or number == 0:
        return 'is a double digit'
    else:
        return 'is not a double digit'


def is_even_second_func(number):
    if number % 2 == 0 or number == 0:
        result = 'is a double digit'
    else:
        result = 'is not a double digit'
    return result


def main():
    print(is_even(4))
    print(is_even_second_func(3))


if __name__ == '__main__':
    main()
