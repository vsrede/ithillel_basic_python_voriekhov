def horse_move(start, end):
    letters_board = 'abcdefgh'
    if abs(int(start[1]) - int(end[1])) == 2:
        for i in range(len(letters_board)):
            if letters_board[i] == start[0]:
                idx_letters_start = i
            if letters_board[i] == end[0]:
                idx_letters_end = i
        if abs(idx_letters_start - idx_letters_end) == 1:
            return True
        else:
            return False
    else:
        return False


def main():
    start_step = input('Enter start moving ')
    end_step = input('Enter where to move ')
    print(horse_move(start_step, end_step))


if __name__ == '__main__':
    main()
