def lchain(*iterables):  # returns list
    result = list()

    for num in iterables:
        result.extend(num)

    return result


def main():
    exeperement = ([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
    print(lchain(*exeperement))
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


if __name__ == '__main__':
    main()
