import tkinter
from math import sin, cos, radians

x0, y0 = 190, 130

def rucicka(uhol, dlzka, hrubka, farba):
    x = x0 + dlzka * cos(radians(uhol))
    y = y0 + dlzka * sin(radians(uhol))
    canvas.create_line(x0, y0, x, y, width=hrubka, fill=farba, arrow='last')

def hodinky(hod, min, sek):
    canvas.create_oval(x0-100, y0-100, x0+100, y0+100, fill='white')
    rucicka((hod-3+min/60)*30, 60, 10, 'gray')
    rucicka((min-15)*6, 70, 6, 'black')
    rucicka((sek-15)*6, 80, 2, 'red')

canvas = tkinter.Canvas()
canvas.pack()

hodinky(8, 55, 10)

tkinter.mainloop()
