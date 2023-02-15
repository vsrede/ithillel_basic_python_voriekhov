def my_func_degree(degree):
    if degree == 0:
        return 1
    return 2*my_func_degree(degree-1)


def main():
    print(my_func_degree(5))
    print(2**5)


if __name__ == '__main__':
    main()
