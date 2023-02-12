def double_digit_first_func(digit):
    if digit % 2 == 0 or digit == 0:
        return 'is a double digit'
    else:
        return 'is not a double digit'


def double_digit_second_func(digit):
    if digit % 2 == 0 or digit == 0:
        parity = 'is a double digit'
    else:
        parity = 'is not a double digit'
    return parity


def main():
    print(double_digit_first_func(5))
    print(double_digit_second_func(3))


if __name__ == '__main__':
    main()
