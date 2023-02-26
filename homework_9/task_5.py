def copydeep(obj):  # returns integer or None
    if isinstance(obj, (int, float, str)):
        return obj

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)

    if isinstance(obj, dict):
        return {copydeep(key): copydeep(value) for key, value in obj.items()}


def main():
    lst1 = ['abf', 1, 2.0, {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}]
    lst2 = copydeep(lst1)
    lst1[3][7] = 999
    print(lst1)
    print(lst2)
    lst3 = 'Hello'


if __name__ == '__main__':
    main()
