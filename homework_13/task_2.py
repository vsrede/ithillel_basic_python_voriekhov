class Circle:

    def __init__(self, radius, x_coordinate, y_coordinate):
        self.radius = radius
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def check_point_in_circle(self, point):
        point_x = point.x_coordinate
        point_y = point.y_coordinate
        if (point_x - self.x_coordinate) ** 2 + (point_y - self.y_coordinate) ** 2 <= self.radius ** 2:
            return True
        else:
            return False


class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


my_circle_one = Circle(50, 1, 1)
my_point_one = Point(-50, -50)

my_circle_two = Circle(5, 4, 2)
my_point_two = Point(1, 3)


def main():

    print(my_circle_one.check_point_in_circle(my_point_one))
    print(my_circle_two.check_point_in_circle(my_point_two))


if __name__ == '__main__':
    main()


    
