def copydeep(obj):  # returns integer or None
    lst2 = list()
    for i in range(len(obj)):
        if isinstance(obj[i], (str, int, float)):
            lst2.append(obj[i])
        elif isinstance(obj[i], (list, tuple)):
            lst2.append([])
            for k in range(len(obj[i])):
                lst2[i].append(obj[i][k])

    return lst2


def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(lst1[3], lst2[3])  # ['b', 0] ['b']


if __name__ == '__main__':
    main()
