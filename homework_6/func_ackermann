def func_ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0 and m > 0:
        return func_ackermann(m - 1, 1)
    else:
        return func_ackermann(m - 1, func_ackermann(m, n - 1))


def main():
    m, n = int(input('Enter m ')), int(input('Enter n '))
    print(func_ackermann(m, n))


if __name__ == '__main__':
    main()
