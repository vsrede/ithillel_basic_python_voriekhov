def calculate_wheat_chess_position(kilograms):
    weight_summ = 0.000035
    chessboard_letters = 'abcdefgh'
    cell = 0
    for i in range(1, 65):
        weight_summ = weight_summ * 2
        if weight_summ > kilograms:
            cell = i
            break
    letters = chessboard_letters[cell//8]
    return chessboard_letters[cell//8], cell % 8


def main():
    n = float(input('Enter '))
    print(*calculate_wheat_chess_position(n), sep='')


if __name__ == '__main__':
    main()
