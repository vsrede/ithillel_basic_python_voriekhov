def copydeep(obj, memory=None):  # returns integer or None
    memory = {}
    if id(obj) in memory:
        return obj
    else:
        new_list = []
        memory[id(obj)] = new_list
        for idx, elem in enumerate(obj):
            if isinstance(obj, list):
                copydeep(elem, memory)
            else:
                new_list.append(elem)

        #return [copydeep(x) for x in obj]
    if isinstance(obj, (int, float, str)):
        return obj
    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)
    if isinstance(obj, dict):
        return dict(copydeep(x) for x in obj.items())


def main():
    lst1 = ['1']
    lst1.append(lst1)
    lst2 = copydeep(lst1)
    print(lst2)


if __name__ == '__main__':
    main()
