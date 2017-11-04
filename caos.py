from Tkinter import *

master = Tk()
miCanvas = Canvas(master, width=600, height=600)
miCanvas.pack()
#Dibujo los lados del triangulo
miCanvas.create_line(100, 500, 500, 500)
miCanvas.create_line(500, 500, 300, 600 - ((400**2 - 200**2)**(0.5))-100)
miCanvas.create_line(300, 600 - ((400**2 - 200**2)**(0.5))-100,100,500)

mainloop()
