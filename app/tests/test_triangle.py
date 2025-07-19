
from app.src.triangle import Triangle, Point


class TestTriangle:
    def test_create_from_list(self):
        vertices = [(0, 0), (1, 0), (0, 1)]

        triangle = Triangle.create_from_list(vertices)
        
        assert len(triangle.vertices) == 3
        assert triangle.vertices[0] == Point(0, 0)
        assert triangle.vertices[1] == Point(1, 0)
        assert triangle.vertices[2] == Point(0, 1)

    def test_is_inside(self):
        vertices = [(0, 0), (2, 0), (1, 2)]
        triangle = Triangle.create_from_list(vertices)

        is_inside = triangle.is_inside(Point(1, 1))

        assert is_inside is True

    def test_generate_inside_point(self):
        vertices = [(0, 0), (2, 0), (1, 2)]
        triangle = Triangle.create_from_list(vertices)

        point = triangle.generate_inside_point()

        assert triangle.is_inside(point) is True
    
    def test_get_vertex(self):
        vertices = [(0, 0), (2, 0), (1, 2)]
        triangle = Triangle.create_from_list(vertices)
        
        vertex = triangle.get_vertex(0)

        assert vertex == Point(0, 0)
    
    def test_get_random_vertex(self):
        vertices = [(0, 0), (2, 0), (1, 2)]
        triangle = Triangle.create_from_list(vertices)

        random_vertex = triangle.get_random_vertex()

        assert random_vertex in triangle.vertices
        
        