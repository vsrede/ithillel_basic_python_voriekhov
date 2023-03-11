import random
import secrets
import string


def gen_pass(lenght):
    value_pass = [*string.ascii_lowercase,
                  *string.ascii_uppercase,
                  *string.digits,
                  '_']
    password = list()
    for i in range(lenght):
        password.append(value_pass[secrets.randbelow(len(value_pass))])
    while True:
        flag = 0

        if any(x.islower() for x in password):
            flag += 1
        else:
            password[random.randint(0, lenght)] = string.ascii_lowercase[secrets.randbelow(len(string.ascii_lowercase))]

        if any(x.isupper() for x in password):
            flag += 1
        else:
            password[random.randint(0, lenght)] = string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))]

        if any(x.isdigit() for x in password):
            flag += 1
        else:
            password[random.randint(0, lenght)] = string.digits[secrets.randbelow(len(string.digits))]

        for i in range(1, lenght):
            if password[i] == password[i - 1]:
                password[i] = value_pass[secrets.randbelow(len(value_pass))]
                flag = 0
                break

        if flag == 3:
            return ''.join(password)


def main():
    length_pass = 0
    while length_pass < 8:
        length_pass = int(input('Enter the length for password '))
        if length_pass < 8:
            print('You length can be more then 7')
    print(gen_pass(length_pass))


if __name__ == '__main__':
    main()

