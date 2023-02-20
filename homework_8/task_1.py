def index(lst, elem):  # returns integer or None
    idx = -1
    for i in range(len(lst)):
        if elem == lst[i]:
            idx = i
            break
    if idx >= 0:
        return idx
    else:
        return None


def main():
    my_list = ['a', 2, None, 'PuHu']
    print(index(my_list, 'a'))
    print(index(my_list, 2))
    print(index(my_list, 'Hillel'))


if __name__ == '__main__':
    main()
