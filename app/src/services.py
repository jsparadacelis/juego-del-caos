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
        return self._ray_casting(point)
    
    def _ray_casting(self, point: Point) -> bool:
        count = 0
        for i in range(len(self.vertices)):
            v1 = self.vertices[i]
            v2 = self.vertices[(i + 1) % len(self.vertices)]
            if ((v1.y > point.y) != (v2.y > point.y)) and \
               (point.x < (v2.x - v1.x) * (point.y - v1.y) / (v2.y - v1.y) + v1.x):
                count += 1
        return count % 2 == 1
    
    @classmethod
    def create_from_list(cls, vertices: list[tuple[int, int]]) -> "Polygon":
        return cls(vertices=[Point(x, y) for x, y in vertices])

    def get_vertex(self, index: int) -> Point:        
        if 0 <= index < len(self.vertices):
            return self.vertices[index]

        raise IndexError("Vertex index out of range")


def generate_initial_point(poligono: Polygon) -> Point:
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
