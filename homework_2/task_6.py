from math import cos, tan
number = int(input('Insert the number '))# радианы
tangens = ((1 / (cos(number)**2)) -1)**0.5
tangens_2 = ((1 - cos(2 * number))/(1 + cos(2 * number)))**0.5
print(tangens, tangens_2, tan(number))#тангенс может быть отрицательный в 2 и 4 плоскостях (нужно условие делать)
