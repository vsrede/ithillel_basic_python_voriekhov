def main():
    original_list_1 = [5, '9', 0, '452', 6.5, '6', 1, 2]
    print(original_list_1)
    sorted_list_1 = sorted(original_list_1, key=float)
    print(sorted_list_1)

    original_list_2 = [472, 326, 1, 999.0, '1101000', '99', 9, '20', 863, '0']
    print(original_list_2)
    sorted_list_2 = sorted(original_list_2, key=lambda num: str(num)[0])
    print(sorted_list_2)


if __name__ == '__main__':
    main()
