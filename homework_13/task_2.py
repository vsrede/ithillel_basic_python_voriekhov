class Circle:

    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def check_point_in_circle(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


my_circle_one = Circle(50, 1, 1)
my_point_one = Point(-50, -50)

my_circle_two = Circle(5, 4, 2)
my_point_two = Point(1, 3)


def main():
    print(my_circle_one.check_point_in_circle(my_point_one))
    print(my_circle_two.check_point_in_circle(my_point_two))


if __name__ == '__main__':
    main()


