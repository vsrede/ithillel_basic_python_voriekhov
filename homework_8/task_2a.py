def copydeep(obj):  # returns integer or None
    if isinstance(obj, (int, float, str)):
        return obj

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)


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
