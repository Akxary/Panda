class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, a):
        self._width = a
        self._height = a

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


if __name__ == '__main__':
    def use_it(rc: Rectangle):
        # API problem. Liskov Substitution Principle distracted
        w = rc.width
        rc.height = 10
        expected = int(w*10)
        print(f'Expected {expected}, got {rc.area()}')

rct = Rectangle(2, 3)
use_it(rct)

sq = Square(5)
use_it(sq)