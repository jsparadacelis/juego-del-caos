from app.src.triangle import Point

class TestPoint:

    def test_returns_mid_point_between_two_points(self):
        p1 = Point(0, 0)
        p2 = Point(2, 2)

        mid = p1.get_mid_point(p2)

        assert mid.x == 1
        assert mid.y == 1