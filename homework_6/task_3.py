def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    z1 = (-b + discriminant**0.5) / 2
    z2 = (-b - discriminant**0.5) / 2
    return z1, z2


def main():
    a = int(input('Input a '))
    b = int(input('Input b '))
    c = int(input('Input c '))
    z1, z2 = solve_quadratic_equation(a, b, c)
    print(f'z1 = {z1}, z2 = {z2}')


if __name__ == '__main__':
    main()
