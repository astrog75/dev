# Animation qui affiche un cercle toutes les x ms

from tkinter import *
from random import uniform

root = Tk()

stop_animate = False

# Dessine un disque de rayon radius à une position
# aléatoire
def draw_circle():
    global can
    
    radius = 10
    
    x0 = uniform(0, 480)
    y0 = uniform(0, 320)

    can.create_oval(x0, y0, x0 + radius, y0 + radius, fill = "red", outline = "red") 
    can.pack()

    if stop_animate == False:
        root.after(100, draw_circle)

def stop():
    global stop_animate
    stop_animate = True
    print("test")

def delete():
    global can
    pts = [(0, 0), (0, 480), (320, 480), (320, 0)]
    can.create_polygon(pts, fill = "white", outline = "white")

def animate():
    global stop_animate, can
    width = 480
    height = 320
    can = Canvas(root, width = width, height = height, bg ='white')
    if (stop_animate == True):
        stop_animate = False
        draw_circle()

but_start = Button(root, text = "Start", command = animate)
but_stop = Button(root, text = "Stop", command = stop)
but_delete = Button(root, text = "Delete", command = delete)

but_start.pack()
but_stop.pack()
but_delete.pack()

root.mainloop()
