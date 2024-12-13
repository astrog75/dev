# Simulation de feux de forêt grâceà un automate cellulaire
# Chaque cellule est dans l'un des 4 états suivants :
# "vide" en blanc
# "foret" en vert
# "en feu" en rouge
# "cendres" en gris
# Règle : si l'une des cellules voisines (N, S, E, W) d'une cellule "foret"
# est "en feu" à l'étape n, la cellule "foret" passe "en feu" à l'étape n+1
# puis en "cendres" à l'étape n+2

# A améliorer :
# Animation

from tkinter import *
from random import randint
from math import floor

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Simulation de feux de forêt")

# taille de la grille
size = 20

# Choix de la probabilité qu'une cellule soit initialement une "foret"
p = 0.59274605079210

# Fonction simulant un lancer de pièce truquée, avec une probabilité p
# d'avoir pile
def rand_state(p):
    n = randint(1, 10000)
    if n < p*10000:
        return 'green'
    else:
        return 'white'
    

# fonction qui change l'état d'une cellule
def change_state(i, j):
    if cells[i][j]["background"] == 'green':
        cells[i][j]["background"] = 'red'
    elif cells[i][j]["background"] == 'red':
        cells[i][j]["background"] = 'gray'
##    elif cells[i][j]["background"] == 'gray':
##        cells[i][j]["background"] = 'white'
    elif cells[i][j]["background"] == 'white':
        cells[i][j]["background"] = 'green'


# Création de la grille de cellules
# Initialement, chaque cellule est soit "foret", soit "vide"
cells = [] 
for i in range(size):
    current_line = []
    for j in range(size):
        button = Button(fenetre, height = 1, width = 1,
                        borderwidth=3,
                        background = rand_state(p),
                        relief = 'groove',
                        command = lambda i = i, j = j:change_state(i, j))
        button.grid(row = i, column = j)
        current_line.append(button)
    cells.append(current_line)

def reset():
    for i in range(size):
        for j in range(size):
            cells[i][j]["background"] = rand_state(p)

# Retourne 1 si l'un des voisin de la cellule est en feu
# 0 sinon
def burning_neighbor(i, j):
    # Gestion des bords
    if (i == 0): # 1ere ligne
        if (j == 0): # Coin supérieur gauche
            if (cells[0][1]["background"] == 'red'):
                return 1
            if (cells[1][0]["background"] == 'red'):
                return 1
        elif (j == size-1): # Coin supérieur droit
            if (cells[0][j-1]["background"] == 'red'):
                return 1
            if (cells[1][j]["background"] == 'red'):
                return 1
        else: # On est sur la 1ere ligne, mais pas dans les coins
            if (cells[0][j-1]["background"] == 'red'):
                return 1
            if (cells[1][j]["background"] == 'red'):
                return 1
            if (cells[0][j+1]["background"] == 'red'):
                return 1
    elif (i == size-1): # dernière ligne
        if (j == 0): # Coin inférieur gauche
            if (cells[i-1][0]["background"] == 'red'):
                return 1
            if (cells[i][1]["background"] == 'red'):
                return 1
        elif (j == size-1): # Coin inférieur droit
            if (cells[i-1][j]["background"] == 'red'):
                return 1
            if (cells[i][j-1]["background"] == 'red'):
                return 1
        else: # On est sur la dernière ligne, mais pas dans les coins
            if (cells[i][j-1]["background"] == 'red'):
                return 1
            if (cells[i-1][j]["background"] == 'red'):
                return 1
            if (cells[i][j+1]["background"] == 'red'):
                return 1
    elif (i > 0 and i < size-1): # ligne quelconque, ni la 1ere, ni la dernière
        if (j == 0):
            if (cells[i-1][0]["background"] == 'red'):
                return 1
            if (cells[i][1]["background"] == 'red'):
                return 1
            if (cells[i+1][0]["background"] == 'red'):
                return 1
        elif (j == size-1):
            if (cells[i-1][j]["background"] == 'red'):
                return 1
            if (cells[i][j-1]["background"] == 'red'):
                return 1
            if (cells[i+1][j]["background"] == 'red'):
                return 1
        else: # Cas général
            if (cells[i-1][j]["background"] == 'red'): # North
                return 1
            if (cells[i][j-1]["background"] == 'red'): # West
                return 1
            if (cells[i+1][j]["background"] == 'red'): # South
                return 1
            if (cells[i][j+1]["background"] == 'red'): # East
                return 1

coord_cells_to_update = []
def simu():
    global coord_cells_to_update
    coord_cells_to_update = []
    for i in range(size):
        for j in range(size):
            if cells[i][j]["background"] == "green" and burning_neighbor(i, j) == 1:
                coord_cells_to_update.append((i, j))
            elif cells[i][j]["background"] == "red":
                coord_cells_to_update.append((i, j))
            elif cells[i][j]["background"] == "grey":
                coord_cells_to_update.append((i, j))

    for coord_cell in coord_cells_to_update:
        change_state(coord_cell[0], coord_cell[1])

    print("simu : " + str(len(coord_cells_to_update)))

def animate():
    simu()
    global coord_cells_to_update
    while len(coord_cells_to_update) != 0:
        fenetre.after(500, simu)
        

# Buttons
but_start = Button(fenetre, height = 2, borderwidth=3,
                   text = "Start",
                   command = simu)
but_start.grid(row = size, columnspan = 3, column = floor(size/2) - 4)

but_reset = Button(fenetre, height = 2, borderwidth=3,
                   text = "Reset",
                   command = reset)
but_reset.grid(row = size, columnspan = 3, column = floor(size/2))

but_quit = Button(fenetre, height = 2, borderwidth=3,
                   text = "Quit",
                   command = fenetre.destroy)
but_quit.grid(row = size, columnspan = 3, column = floor(size/2) + 4)

fenetre.mainloop()
    
    
