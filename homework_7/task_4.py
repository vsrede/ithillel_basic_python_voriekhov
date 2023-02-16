def sum_symbol_codes(first, last):
    summ_character = 0
    for i in range(ord(first), ord(last) + 1):
        summ_character += i
    return summ_character


def main():
    first = input('Enter first character ')
    last = input('Enter last character ')
    print(sum_symbol_codes(first, last))


if __name__ == '__main__':
    main()
