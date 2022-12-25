from Without_cache_1 import Rectangle, Line, Point, draw_point

class LineToPointAdapter:
    cache = {}

    def __init__(self, line: Line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()

        print(f': Generating points for line '
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

def draw(rcs):
    print('\n\n---Drawing some stuff ---\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)
