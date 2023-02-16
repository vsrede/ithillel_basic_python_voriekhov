def main():
    idx_fib = 20
    first_digit = 1
    second_digit = 0
    fib = 0
    for i in range(idx_fib):
        fib = first_digit + second_digit
        second_digit, first_digit = second_digit + first_digit, second_digit
    print(fib)


if __name__ == '__main__':
    main()
