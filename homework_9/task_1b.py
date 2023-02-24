from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    random_list = []
    for i in range(num_limit):
        random_list.append(randint(lower_bound, upper_bound))
    min_value, max_value = random_list[0], random_list[0]
    for i in range(num_limit):
        if random_list[i] > max_value:
            max_value = random_list[i]
        elif random_list[i] < min_value:
            min_value = random_list[i]
    return max_value - min_value


def main():
    num_limit = int(input('Enter len '))
    lower_bound = int(input('Enter min value for list '))
    upper_bound = int(input('Enter max value for list '))
    print(diff_min_max(num_limit, lower_bound, upper_bound))
    

if __name__ == '__main__':
    main()
