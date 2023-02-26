def group_by_surname(list_of_enrollees):  # returns 4 ints
    a_i_enrollee, j_p_enrollee, q_t_enrollee, u_z_enrollee = 0, 0, 0, 0
    # characters acc UTF(dec)
    a_dec, i_dec, j_dec, p_dec, q_dec, t_dec = 65, 73, 74, 80, 81, 84

    for num in list_of_enrollees:
        first_let = ord(num[num.find(' ') + 1].upper())
        if a_dec <= first_let <= i_dec:
            a_i_enrollee += 1
        elif j_dec <= first_let <= p_dec:
            j_p_enrollee += 1
        elif q_dec <= first_let <= t_dec:
            q_t_enrollee += 1
        else:
            u_z_enrollee += 1

    return a_i_enrollee, j_p_enrollee, q_t_enrollee, u_z_enrollee


def main():
    name = ['Vadim Vadimov', 'Oleg Olegov', 'Britney Spears', 'Artem Artemov', 'Oleg Olegov']
    print(group_by_surname(name))


if __name__ == '__main__':
    main()
