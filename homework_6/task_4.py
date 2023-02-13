def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    d = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    return r1 + r2 > d


def main():
    x1 = int(input('Input x1 '))
    y1 = int(input('Input y1 '))
    r1 = int(input('Input r1 '))
    x2 = int(input('Input x2 '))
    y2 = int(input('Input y2 '))
    r2 = int(input('Input r2 '))
    if circles_intersect(x1, y1, r1, x2, y2, r2):
        print('circles intersect')
    else:
        print('circles do not intersect')


if __name__ == '__main__':
    main()
