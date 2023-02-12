def fibonacci(n, digit=0, pre_digit=1):
    if n == 1:
        return digit
    return fibonacci(n - 1, digit=digit + pre_digit, pre_digit=digit)


def main():
    print(fibonacci(10))


if __name__ == '__main__':
    main()
