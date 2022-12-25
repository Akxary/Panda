import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    class PointFactory:

        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    factory = PointFactory()

if __name__ == '__main__':
    p2 = Point.factory.new_cartesian_point()