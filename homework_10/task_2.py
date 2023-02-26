import secrets
import string


def gen_pass(lenght):
    value_pass = [string.ascii_lowercase,
                  string.ascii_uppercase,
                  string.digits,
                  '_']
    password = list()
    key = 0

    for i in range(lenght):
        password.append(value_pass[key][secrets.randbelow(len(value_pass[key]))])
        if i >= 1:
            while password[i] == password[i-1]:
                password[i] = value_pass[0][secrets.randbelow((len(value_pass[0])))]
        if key < 3:
            key += 1
        else:
            key = secrets.randbelow(3)
            
    password = ''.join(password)
    return password


def main():
    length_pass = int(input('Enter the length for password '))
    print(gen_pass(length_pass))


if __name__ == '__main__':
    main()
