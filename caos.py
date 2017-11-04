from logica import *
from Tkinter import *

log = logica()


master = Tk()
miCanvas = Canvas(master, width=600, height=600)
miCanvas.pack()
#Dibujo los lados del triangulo
miCanvas.create_line(100, 500, 500, 500)
miCanvas.create_line(500, 500, 300, 500 - ((400**2 - 200**2)**(0.5)))
miCanvas.create_line(300, 600 - ((400**2 - 200**2)**(0.5))-100,100,500)
poligono = [(100,500),(500,500),(300, 600 - ((400**2 - 200**2)**(0.5))-100)]
punto = log.generaCoorInicial(poligono)
circulo = miCanvas.create_oval(punto[0], punto[1], punto[0]+5, punto[1]+5, fill='black')
mainloop()
