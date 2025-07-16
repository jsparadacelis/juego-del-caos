from typing import Tuple
from app.src.logica import *
from tkinter import *
from time import sleep


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

    poligono = [(100, 500), (500, 500), (300, 600 - ((400**2 - 200**2) ** (0.5)) - 100)]

    p0 = generate_initial_coordinate(poligono)
    v = poligono[get_random_vertix()]
    pm = mid_point(v[0], v[1], p0[0], p0[1])
    canvas.create_oval(pm[0] - 2.5, pm[1] + 2.5, pm[0] + 2.5, pm[1] - 2.5, fill="black")

    cont = 0
    while cont < 1000:
        v = poligono[get_random_vertix()]
        pm = mid_point(v[0], v[1], pm[0], pm[1])
        canvas.create_oval(
            pm[0] - 2.5, pm[1] + 2.5, pm[0] + 2.5, pm[1] - 2.5, fill="blue"
        )
        cont = cont + 1
    master.mainloop()


if __name__ == "__main__":
    main()
