import math
a = 1
b = 5
c = 6
x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
print(x1, x2, sep=' ')
