from logica import *
from tkinter import *
from time import sleep


def main() -> None:
    log = logica()

    master = Tk()
    miCanvas = Canvas(master, width=600, height=600)
    miCanvas.pack()
    # Dibujo los lados del triangulo
    miCanvas.create_line(100, 500, 500, 500)
    miCanvas.create_line(500, 500, 300, 500 - ((400**2 - 200**2) ** (0.5)))
    miCanvas.create_line(300, 600 - ((400**2 - 200**2) ** (0.5)) - 100, 100, 500)
    poligono = [(100, 500), (500, 500), (300, 600 - ((400**2 - 200**2) ** (0.5)) - 100)]

    p0 = log.generaCoorInicial(poligono)
    v = poligono[log.verticeAleatorio()]
    pm = log.puntoMedio(v[0], v[1], p0[0], p0[1])
    miCanvas.create_oval(
        pm[0] - 2.5, pm[1] + 2.5, pm[0] + 2.5, pm[1] - 2.5, fill="black"
    )

    cont = 0
    while cont < 1000:
        v = poligono[log.verticeAleatorio()]
        pm = log.puntoMedio(v[0], v[1], pm[0], pm[1])
        miCanvas.create_oval(
            pm[0] - 2.5, pm[1] + 2.5, pm[0] + 2.5, pm[1] - 2.5, fill="blue"
        )
        cont = cont + 1
    master.mainloop()

if __name__ == "__main__":
    main()
