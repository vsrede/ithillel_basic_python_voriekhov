from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    random_list = []
    for i in range(num_limit):
        random_list.append(randint(lower_bound, upper_bound))
    return max(random_list) - min(random_list)


def main():
    num_limit = int(input('Enter len '))
    lower_bound = int(input('Enter min value for list '))
    upper_bound = int(input('Enter max value for list '))
    print(diff_min_max(num_limit, lower_bound, upper_bound))


if __name__ == '__main__':
    main()
