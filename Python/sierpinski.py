from tkinter import * 
import random

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

width = 700
height = 700

# canvas
canvas = Canvas(fenetre, width=width, height=height, background='yellow')
canvas.pack()

p1 = (width//2, height//4)
p2 = (width//4, 3*height//4)
p3 = (3*width//4, 3*height//4)

for p in [p1,p2,p3]:
    s = 5
    canvas.create_oval(p[0]-s//2, p[1]-s//2, p[0]+s//2, p[1]+s//2, fill="red")

fp = (width//2, 2*height//4)
canvas.create_oval(fp[0]-s//2, fp[1]-s//2, fp[0]+s//2, fp[1]+s//2, fill="red")

idx = random.randint(0,2)
p = [p1,p2,p3][idx]

# canvas.create_line(p[0],p[1],fp[0],fp[1])

middle = (p[0]+fp[0])//2, (p[1]+fp[1])//2
canvas.create_oval(middle[0]-s//2, middle[1]-s//2, middle[0]+s//2, middle[1]+s//2, fill="red")

nb_points = 10000
while nb_points > 0:
    idx = random.randint(0,2)
    p = [p1,p2,p3][idx]

    # canvas.create_line(p[0],p[1],fp[0],fp[1])

    middle = (p[0]+fp[0])//2, (p[1]+fp[1])//2
    canvas.create_oval(middle[0]-s//2, middle[1]-s//2, middle[0]+s//2, middle[1]+s//2, fill="red")
    
    fp = middle
    
    nb_points -= 1

fenetre.mainloop()