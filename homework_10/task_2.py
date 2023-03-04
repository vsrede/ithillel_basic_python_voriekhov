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
            password[random.randint(0, lenght)] = random.choice(list(string.ascii_lowercase))

        if any(x.isupper() for x in password):
            flag += 1
        else:
            password[random.randint(0, lenght)] = random.choice(list(string.ascii_uppercase))

        if any(x.isdigit() for x in password):
            flag += 1
        else:
            password[random.randint(0, lenght)] = random.choice(list(string.digits))

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
