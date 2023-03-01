def copydeep(obj, memory=None):  # returns integer or None
    if memory is None:
        memory = {}
    if id(obj) in memory:
        return memory[id(obj)]
    if isinstance(obj, list):
        lst = list()
        memory[id(obj)] = lst
        for elem in obj:
            lst.append(copydeep(elem, memory))
        return lst

    if isinstance(obj, dict):
        dict_rec = {}
        memory[id(obj)] = dict_rec
        for key, value in obj.items():
            dict_rec[copydeep(key, memory)] = copydeep(value, memory)
        return dict_rec

    if isinstance(obj, (int, float, str)):
        return obj
    
    return obj


def main():
    lst1 = [1, 2, 3]
    lst1.append(lst1)
    lst2 = copydeep(lst1)
    print(lst1)
    print(lst2)
    lst3 = 'Hello'


if __name__ == '__main__':
    main()
