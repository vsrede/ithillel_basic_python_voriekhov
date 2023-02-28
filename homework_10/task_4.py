from random import randint


def get_str():
    while True:
        choice_game = input("If you wan't guess a number enter 'i', if me enter 'y': ")
        if choice_game == "i" or choice_game == "y":
            print("Let's start")
            break
        else:
            print("You input is not correct, repeat please")
    return choice_game


def get_integer(choice):
    digit_list = [x for x in range(1, 101)]
    if choice == 'i':
        digit = randint(1, 3)
        answer = 0
        while digit != answer:
            answer = int(input("Enter you digit: "))
            if answer == digit:
                print("You win!")
            elif answer is not digit_list:
                print("You input is not correct, repeat please")
            else:
                "Try again"
    elif choice == 'y':
        low = 1
        high = 99
        while low <= high:
            mid = (low + high) // 2
            digit = digit_list[mid]
            answer = input(f"Is it your number {digit}? If yes enter 'y', "
                           f"if now please point your number bigger or smaller? "
                           f"If smaller enter 's', if bigger enter 'b': ")
            if answer == 'y':
                print("Yes, i am winner")
                break
            elif answer == 's':
                high = mid - 1
            elif answer == 'b':
                low = mid + 1
            else:
                print("Your answer doesn't correct, please try again")


def main():
    while True:
        active = input("Do you play the game? If yes enter 'y', if now enter 'n': ")
        if active == 'y':
            get_integer(get_str())
        elif active == 'n':
            print('Bye')
            break
        else:
            continue


if __name__ == '__main__':
    main()
