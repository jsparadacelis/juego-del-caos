from typing import Tuple
from triangle import Point, Triangle
from tkinter import Tk, Canvas


def setup_canvas(width: int = 600, height: int = 600) -> Tuple[Tk, Canvas]:
    _master = Tk()
    _canvas = Canvas(_master, width=width, height=height)
    _canvas.pack()

    _canvas.create_rectangle(0, 0, width, width, fill="white")
    _canvas.create_text(width/2, 20, text="Sierpinski", font=("Arial", 16))

    return _master, _canvas


def add_triangle_to_canvas(canvas: Canvas, triangle: Triangle) -> None:
    first_vertex = triangle.vertices[0]
    second_vertex = triangle.vertices[1]
    third_vertex = triangle.vertices[2]

    canvas.create_line(
        first_vertex.x, first_vertex.y,
        second_vertex.x, second_vertex.y,
        fill="black",
    )
    canvas.create_line(
        second_vertex.x, second_vertex.y,
        third_vertex.x, third_vertex.y,
        fill="black",
    )
    canvas.create_line(
        third_vertex.x, third_vertex.y,
        first_vertex.x, first_vertex.y,
        fill="black",
    )

def add_point_to_canvas(canvas: Canvas, point: Point, color: str = "blue") -> None:
    canvas.create_oval(
        point.x - 2.5,
        point.y + 2.5,
        point.x + 2.5,
        point.y - 2.5,
        fill=color,
    )


def main() -> None:
    master, canvas = setup_canvas()

    vertices = [(100, 500), (500, 500), (200, 500 - ((400**2 - 200**2) ** (0.5)))]
    triangle = Triangle.create_from_list(vertices)

    add_triangle_to_canvas(canvas, triangle)

    initial_point = triangle.generate_inside_point()

    random_vertex = triangle.get_random_vertex()
    mid_point = initial_point.get_mid_point(random_vertex)

    cont = 0
    while cont < 1e4:
        random_vertex = triangle.get_random_vertex()
        mid_point = mid_point.get_mid_point(random_vertex)
        add_point_to_canvas(canvas, mid_point)
        cont = cont + 1
    master.mainloop()


if __name__ == "__main__":
    main()
