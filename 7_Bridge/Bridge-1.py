# Соединение двух сущностей через промежуточную абстракцию
# circle & square
# vector & raster
from abc import ABC


# VectorCircle VectorSquare RasterCircle RasterSquare
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ bad idea

class Renderer(ABC):
    def render_circle(self, radius):
        pass
    # render_square
    # нарушение OCP, но избегаем взрывного роста сложности

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

class RasterRender(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer # bridge is here
    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, render, radius):
        super().__init__(render)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius) # bridge is here

    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRender()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()