from src.services import Polygon, Point


class TestServices:
    def test_should_return_true_for_point_inside_polygon(self):
        vertices = [Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)]
        polygon = Polygon(vertices=vertices)
        
        is_inside = polygon.is_inside(Point(3, 3))

        assert is_inside
    
    def test_should_return_false_for_point_outside_polygon(self):
        vertices = [Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)]
        polygon = Polygon(vertices=vertices)
        
        is_inside = polygon.is_inside(Point(6, 6))

        assert not is_inside
    
    def test_should_create_polygon_from_list_of_tuples(self):
        vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
        polygon = Polygon.create_from_list(vertices)

        assert len(polygon.vertices) == 4
        assert polygon.vertices[0] == Point(0, 0)
        assert polygon.vertices[1] == Point(5, 0)
        assert polygon.vertices[2] == Point(5, 5)
        assert polygon.vertices[3] == Point(0, 5)

    def test_should_get_a_vertex_from_polygon(self):
        vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
        polygon = Polygon.create_from_list(vertices)

        vertex = polygon.get_vertex(0)

        assert vertex in polygon.vertices
        assert isinstance(vertex, Point)
