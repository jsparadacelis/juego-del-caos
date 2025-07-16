from random import randint


class logica:
    def generaCoorInicial(self, poligono):
        puntoAdentro = False
        while puntoAdentro == False:
            h = int(((400**2 - 200**2) ** (0.5)))
            y = randint(500 - h, 500)
            x = randint(100, 500)
            puntoAdentro = self.puntoEnPoligono(x, y, poligono)
        return x, y

    def puntoEnPoligono(self, x, y, poligono):
        puntoAdentro = False
        i = 0
        j = len(poligono) - 1
        for i in range(len(poligono)):
            if (poligono[i][1] < y and poligono[j][1] >= y) or (
                poligono[j][1] < y and poligono[i][1] >= y
            ):
                if (
                    poligono[i][0]
                    + (y - poligono[i][1])
                    / (poligono[j][1] - poligono[i][1])
                    * (poligono[j][0] - poligono[i][0])
                    < x
                ):
                    puntoAdentro = not puntoAdentro
            j = i
        return puntoAdentro

    def verticeAleatorio(self):
        return randint(0, 2)

    def puntoMedio(self, xv, yv, xp, yp):
        x = (xv + xp) / 2
        y = (yv + yp) / 2
        return x, y
