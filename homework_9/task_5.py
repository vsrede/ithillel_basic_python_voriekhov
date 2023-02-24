def group_by_surname(list_of_enrollees): # returns 4 ints
    a_i_enrollee, j_p_enrollee, q_t_enrollee, u_z_enrollee = 0, 0, 0, 0
    for num in list_of_enrollees:
        idx = str(num).find(' ') + 1
        if 65 <= ord(str(num)[idx]) <= 73:
            a_i_enrollee += 1
        elif 74 <= ord(str(num)[idx]) <= 80:
            j_p_enrollee += 1
        elif 81 <= ord(str(num)[idx]) <= 84:
            q_t_enrollee += 1
        else:
            u_z_enrollee += 1
    return a_i_enrollee, j_p_enrollee, q_t_enrollee, u_z_enrollee


def main():
        name = ['Vadim Vadimov', 'Oleg Olegov', 'Britney Spears', 'Artem Artemov', 'Oleg Olegov']
        print(group_by_surname(name))


if __name__ == '__main__':
    main()


