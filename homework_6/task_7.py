def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_other(n, digit=0, pre_digit=1):
    if n == 1:
        return digit
    return fibonacci_other(n - 1, digit=digit + pre_digit, pre_digit=digit)


def main():
    print(fibonacci(9))
    print(fibonacci_other(10))


if __name__ == '__main__':
    main()
