def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    x1, x2 = None, None
    if discriminant == 0:
        x1 = (-b + discriminant**0.5) / 2*a
        x2 = None
    elif discriminant > 0:
        x1 = (-b + discriminant**0.5) / 2*a
        x2 = (-b - discriminant**0.5) / 2*a
    return x1, x2


def main():
    a = int(input('Input a '))
    b = int(input('Input b '))
    c = int(input('Input c '))
    x1, x2 = solve_quadratic_equation(a, b, c)
    if x1 is None:
        if x2 is None:
            print('no roots')
        else:
            print(f'x = {x2}')
    elif x1 is not None:
        if x2 is None:
            print(f'x = {x1}')
        else:
            print(f'x1 = {x1}, x2 = {x2}')


if __name__ == '__main__':
    main()
