def triangle_square_and_perimeter(a, b):  # returns 2 values
    s = (a * b) / 2
    c = (a**2 + b**2) ** 0.5
    p = a + b + c
    return s, p
katet_1, katet_2 = int(input('Введите катет ')), int(input('Введите следующий катет '))
s, p = triangle_square_and_perimeter(katet_1, katet_2)
print('Площадь =', s)
print('Периметр =', p)
