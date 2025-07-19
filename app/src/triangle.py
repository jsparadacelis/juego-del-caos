from dataclasses import dataclass
import random


@dataclass
class Point:
    x: float
    y: float

    def get_mid_point(self, other: "Point") -> "Point":
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)


@dataclass
class Triangle:
    vertices: list[Point]

    @classmethod
    def create_from_list(cls, vertices: list[tuple[float, float]]) -> "Triangle":
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")

        return cls(vertices=[Point(x, y) for x, y in vertices])

    def is_inside(self, point: Point) -> bool:
        x1, y1 = self.vertices[0].x, self.vertices[0].y
        x2, y2 = self.vertices[1].x, self.vertices[1].y
        x3, y3 = self.vertices[2].x, self.vertices[2].y

        denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        a = ((y2 - y3) * (point.x - x3) + (x3 - x2) * (point.y - y3)) / denominator
        b = ((y3 - y1) * (point.x - x3) + (x1 - x3) * (point.y - y3)) / denominator
        c = 1 - a - b

        return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

    def get_vertex(self, index: int) -> Point:
        if index < 0 or index >= len(self.vertices):
            raise IndexError("Vertex index out of range.")

        return self.vertices[index]

    def get_random_vertex(self) -> Point:
        random_index = random.randint(0, 2)
        return self.get_vertex(random_index)

    def generate_inside_point(self) -> Point:
        min_x = min(vertex.x for vertex in self.vertices)
        max_x = max(vertex.x for vertex in self.vertices)
        min_y = min(vertex.y for vertex in self.vertices)
        max_y = max(vertex.y for vertex in self.vertices)

        while True:
            x = random.uniform(min_x, max_x)
            y = random.uniform(min_y, max_y)
            possible_point = Point(x, y)

            if self.is_inside(possible_point):
                return possible_point
