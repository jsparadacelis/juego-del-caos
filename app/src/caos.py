from typing import Tuple
from triangle import Triangle
from tkinter import Tk, Canvas


def setup_canvas() -> Tuple[Tk, Canvas]:
    _master = Tk()
    _canvas = Canvas(_master, width=600, height=600)
    _canvas.pack()

    _canvas.create_rectangle(0, 0, 600, 600, fill="white")
    _canvas.create_text(300, 20, text="Triángulo de Sierpinski", font=("Arial", 16))

    return _master, _canvas


def add_triangle_to_canvas(canvas: Canvas) -> None:
    canvas.create_polygon(
        100,
        500,
        500,
        500,
        300,
        600 - ((400**2 - 200**2) ** (0.5)) - 100,
        fill="lightgray",
        outline="black",
    )


def main() -> None:
    master, canvas = setup_canvas()

    add_triangle_to_canvas(canvas)

    vertices = [(100, 500), (500, 500), (300, 600 - ((400**2 - 200**2) ** (0.5)) - 100)]
    triangle = Triangle.create_from_list(vertices)

    initial_point = triangle.generate_inside_point()

    random_vertex = triangle.get_random_vertex()
    mid_point = initial_point.get_mid_point(random_vertex)

    canvas.create_oval(
        mid_point.x - 2.5,
        mid_point.y + 2.5,
        mid_point.x + 2.5,
        mid_point.y - 2.5,
        fill="black",
    )

    cont = 0
    while cont < 1e4:
        random_vertex = triangle.get_random_vertex()
        mid_point = mid_point.get_mid_point(random_vertex)
        canvas.create_oval(
            mid_point.x - 2.5,
            mid_point.y + 2.5,
            mid_point.x + 2.5,
            mid_point.y - 2.5,
            fill="blue",
        )
        cont = cont + 1
    master.mainloop()


if __name__ == "__main__":
    main()
