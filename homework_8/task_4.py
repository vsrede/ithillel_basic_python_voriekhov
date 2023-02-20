def gen_primes():  # returns list of ints
    list_from_1_to_100 = list()
    for i in range(1, 101):
        list_from_1_to_100.append(i)
    return list_from_1_to_100


def main():
    my_list = gen_primes()
    print(my_list)


if __name__ == '__main__':
    main()
