from random import randint


def get_max_text(number):
    return max(str(number))


def get_max_digit(number):  # returns list of ints
    max_use_int = 0

    number = int(number)
    while number:
        number, x = divmod(number, 10)
        max_use_int = max(max_use_int, x)
    return max_use_int


def main():
    number = randint(1, 999999999999)
    print(number)
    print(get_max_digit(number))
    print(get_max_text(number))


if __name__ == '__main__':
    main()
