def is_year_high(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def main():
    year = int(input('Input year '))
    if is_year_high(year):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
