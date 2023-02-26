from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound): # returns int
    random_list = []
    double_summ, no_double_summ = 0, 0

    for i in range(num_limit):
        random_list.append(randint(lower_bound, upper_bound))

    for i in range(num_limit):
        if random_list[i] % 2 == 0:
            double_summ += random_list[i]
        else:
            no_double_summ += random_list[i]

    return double_summ - no_double_summ


def main():
    num_limit = int(input('Enter len '))
    lower_bound = int(input('Enter min value for list '))
    upper_bound = int(input('Enter max value for list '))
    print(diff_odd_even(num_limit, lower_bound, upper_bound))


if __name__ == '__main__':
    main()
