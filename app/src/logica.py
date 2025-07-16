from dataclasses import dataclass
from random import randint


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Polygon:
    vertices: list[Point]

    def is_inside(self, point: Point) -> bool:
        return True




def generate_initial_coordinate(poligono):
    puntoAdentro = False
    while not puntoAdentro:
        h = int(((400**2 - 200**2) ** (0.5)))
        y = randint(500 - h, 500)
        x = randint(100, 500)
        puntoAdentro = poligono.is_inside(Point(x, y))
    return x, y



def get_random_vertix():
    return randint(0, 2)


def mid_point(xv, yv, xp, yp):
    x = (xv + xp) / 2
    y = (yv + yp) / 2
    return x, y
