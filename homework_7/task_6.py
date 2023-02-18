def fibonacci_numbers(idx_fib):
    first_digit = 1
    second_digit = 0
    fib = 0
    for i in range(idx_fib):
        fib = first_digit + second_digit
        second_digit, first_digit = second_digit + first_digit, second_digit
    return fib


def main():
    print(fibonacci_numbers(int(input('Enter index '))))


if __name__ == '__main__':
    main()
