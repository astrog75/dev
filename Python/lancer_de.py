from tkinter import *
from random import randint

main = Tk()

def lancer():
    nb = randint(1, 6)
    resultat.set("Résultat : " + str(nb))


main.title('Dé à 6 faces')
main.geometry('300x100+400+400')

resultat = StringVar()

button_start = Button(main, text = "Lancer le dé", command = lancer)
button_start.pack(side = LEFT, padx = 5, pady = 5)

label_resultat = Label(main, textvariable = resultat)
label_resultat.pack(side = LEFT, padx = 5, pady = 5)

main.mainloop()
