def index(lst, elem):  # returns integer or None
    for i in range(len(lst)):
        if elem == lst[i]:
            return i


def main():
    my_list = ['a', 2, None, 'PuHu']
    print(index(my_list, 'a'))
    print(index(my_list, 2))
    print(index(my_list, 'Hillel'))


if __name__ == '__main__':
    main()
