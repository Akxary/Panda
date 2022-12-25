# отказ от массивных конструкторов!
import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # bad way to project
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.y = b
    #         self.x = a
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * math.cos(b)
    #         self.y = a * math.sin(b)
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))
    def __str__(self):
        return f'x:{self.x}, y:{self.y}'
if __name__ == '__main__':
    p = Point(2,3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)