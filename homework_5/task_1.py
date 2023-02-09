from math import cos, pi


def degrees2radians(corner_degree):  # returns float: radians value
    corner_radians = corner_degree * (pi / 180)
    return corner_radians


print(cos(degrees2radians(60)))
print(cos(degrees2radians(45)))
print(cos(degrees2radians(40)))
