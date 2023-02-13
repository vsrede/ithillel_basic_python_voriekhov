def sign(digit):
    if digit > 0:
        return 1
    elif digit < 0:
        return -1
    else:
        return 0


def main():
    digit = int(input('Input digit '))
    print(sign(digit))


if __name__ == '__main__':
    main()
