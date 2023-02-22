def copydeep(obj):  # returns integer or None
    lst2 = list()
    if isinstance(obj, (list, tuple)):
        for i in range(len(obj)):
            if isinstance(obj[i], (str, int, float)):
                lst2.append(obj[i])
            elif isinstance(obj[i], list):
                lst2.append(copydeep(obj[i]))
            elif isinstance(obj[i], tuple):
                lst2.append(tuple(copydeep(obj[i])))
        return lst2
    else:
        return obj


def main():
    lst1 = ['abf', 1, 2.0, ['b', [['hard']]], [('this', ('tuple', '.'))]]
    lst2 = copydeep(lst1)
    lst1[3][1][0].append([])
    lst1[3][1][0].append('deep')
    print(lst1)
    print(lst2)
    lst3 = 'Hello'
    lst4 = copydeep(lst3)
    print(lst4)


if __name__ == '__main__':
    main()
