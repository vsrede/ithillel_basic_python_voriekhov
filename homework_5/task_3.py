from math import pi


def cone_square_and_volume(radius, height):  # returns 2 floats
    s = pi * radius * (radius + (radius**2 + height**2)**0.5) # i counted the total area
    v = (pi * radius**2 * height) / 3
    return s, v


radius, height = int(input()), int(input())
print(cone_square_and_volume(radius, height))
