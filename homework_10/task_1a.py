def copydeep(obj, memory={}, new_list=list()):  # returns integer or None
    if id(obj) in memory:
        return memory

    memory[id(obj)] = new_list
    for idx, elem in enumerate(obj):
        if isinstance(elem, list):
            copydeep(elem, memory, new_list)
        else:
            new_list.append(elem)


    if isinstance(obj, (int, float, str)):
        return obj
    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)
    if isinstance(obj, dict):
        return dict(copydeep(x) for x in obj.items())


def main():
    lst1 = ['1']
    lst1.append(lst1)
    lst1.append(lst1)
    lst2 = copydeep(lst1)
    print(lst1)
    print(lst2)


if __name__ == '__main__':
    main()
