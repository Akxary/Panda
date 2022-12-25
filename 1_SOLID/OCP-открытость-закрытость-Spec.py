from enum import Enum


class Color(Enum):
    GREEN = 1
    BLUE = 2
    YELLOW = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Item:
    def __init__(self, name:str, size:Size, color:Color):
        self.name = name
        self.color = color
        self.size = size

class Specification:
    def is_satisfied(self, item: Item) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(other)

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args=args

    def is_satisfied(self, item: Item) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class Filter:
    pass

class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color
    def is_satisfied(self, item: Item) -> bool:
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size
    def is_satisfied(self, item: Item) -> bool:
        return item.size == self.size

class BetterFilter(Filter):
    @staticmethod
    def filter(items: list[Item], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item
