def horse_move(start, end):
    if abs(ord(start[0]) - ord(end[0])) == 1 \
            and abs(int(start[1]) - int(end[1])) == 2:
        return True
    elif abs(ord(start[0]) - ord(end[0])) == 2 \
            and abs(int(start[1]) - int(end[1])) == 1:
        return True
    else:
        return False


def main():
    start_step = input('Enter start moving ')
    end_step = input('Enter where to move ')
    print(horse_move(start_step, end_step))


if __name__ == '__main__':
    main()
