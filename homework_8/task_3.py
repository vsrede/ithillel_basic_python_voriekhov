def main():
    original_list_1 = [5, '9', 0, '452', 6.5, '6', 1, 2]
    sorted_list_1 = sorted(original_list_1, key=float)
    print(sorted_list_1)

    original_list_2 = ['0', 1, '1101000', '20', 326, 472, 863, 9, '99']
    sorted_list_2 = sorted(original_list_2, key=str)
    print(sorted_list_2)


if __name__ == '__main__':
    main()
