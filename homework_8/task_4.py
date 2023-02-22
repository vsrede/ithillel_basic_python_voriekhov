def gen_primes():  # returns list of ints
    list_from_1_to_100 = list()
    for i in range(1, 101):
        flag = True
        for k in range(2, i):
            if i % k == 0:
                flag = False
        if flag:
            list_from_1_to_100.append(i)
    return list_from_1_to_100


def main():
    my_list = gen_primes()
    print(my_list)
