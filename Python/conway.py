#               A améliorer
# améliorer interface : mieux positionner le bouton start
# pourquoi faut-il réinitialiser count à chaque bloc dans la fonction alive_neigbors ?
# ajouter possibilité de préconfigurer la grille
# améliorer performance
# effets de bord


from tkinter import *
from functools import partial
from math import floor

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Jeu de la vie de Conway")

# Taille de la grille
size = 22

# black == alive
# white == dead

# Transforme une cellule vivante en morte et vice versa
def toggle_bg(i, j):
    if cells[i][j]["background"] == 'black':
        cells[i][j]["background"] = 'white'
    else:
        cells[i][j]["background"] = 'black'


# Création de la grille de boutons
cells = [] 
for ligne in range(size):
    current_line = []
    for colonne in range(size):
        button = Button(fenetre, height = 1, width = 1,
                        borderwidth=3,
                        bg = "white",
                        command = partial(toggle_bg, ligne, colonne))
        button.grid(row=ligne, column=colonne)
        current_line.append(button)
    cells.append(current_line)


# Comptage du nombre de cellules voisines vivantes
def alive_neighbours(i, j):
    count = 0
    # Gestion des bords
    if (i == 0): # 1ere ligne
        if (j == 0): # Coin supérieur gauche
            count = 0
            if (cells[0][1]["background"] == 'black'):
                count += 1
            if (cells[1][0]["background"] == 'black'):
                count += 1
            if (cells[1][1]["background"] == 'black'):
                count += 1
        elif (j == size-1): # Coin supérieur droit
            count = 0
            if (cells[0][j-1]["background"] == 'black'):
                count += 1
            if (cells[1][j-1]["background"] == 'black'):
                count += 1
            if (cells[1][j]["background"] == 'black'):
                count += 1
        else: # On est sur la 1ere ligne, mais pas dans les coins
            count = 0
            if (cells[0][j-1]["background"] == 'black'):
                count += 1
            if (cells[1][j-1]["background"] == 'black'):
                count += 1
            if (cells[1][j]["background"] == 'black'):
                count += 1
            if (cells[1][j+1]["background"] == 'black'):
                count += 1
            if (cells[0][j+1]["background"] == 'black'):
                count += 1
    if (i == size-1): # dernière ligne
        if (j == 0): # Coin inférieur gauche
            count = 0
            if (cells[i-1][0]["background"] == 'black'):
                count += 1
            if (cells[i-1][1]["background"] == 'black'):
                count += 1
            if (cells[i][1]["background"] == 'black'):
                count += 1
        elif (j == size-1): # Coin inférieur droit
            count = 0
            if (cells[i-1][j]["background"] == 'black'):
                count += 1
            if (cells[i-1][j-1]["background"] == 'black'):
                count += 1
            if (cells[i][j-1]["background"] == 'black'):
                count += 1
        else: # On est sur la dernière ligne, mais pas dans les coins
            count = 0
            if (cells[i][j-1]["background"] == 'black'):
                count += 1
            if (cells[i-1][j-1]["background"] == 'black'):
                count += 1
            if (cells[i-1][j]["background"] == 'black'):
                count += 1
            if (cells[i-1][j+1]["background"] == 'black'):
                count += 1
            if (cells[i][j+1]["background"] == 'black'):
                count += 1
    else:
        if (j == 0):
            count = 0
            if (cells[i-1][0]["background"] == 'black'):
                count += 1
            if (cells[i-1][1]["background"] == 'black'):
                count += 1
            if (cells[i][1]["background"] == 'black'):
                count += 1
            if (cells[i+1][1]["background"] == 'black'):
                count += 1
            if (cells[i+1][0]["background"] == 'black'):
                count += 1
        elif (j == size-1):
            count = 0
            if (cells[i-1][j]["background"] == 'black'):
                count += 1
            if (cells[i-1][j-1]["background"] == 'black'):
                count += 1
            if (cells[i][j-1]["background"] == 'black'):
                count += 1
            if (cells[i+1][j-1]["background"] == 'black'):
                count += 1
            if (cells[i+1][j]["background"] == 'black'):
                count += 1
        else: # Cas général
            count = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if (cells[k][l]["background"] == 'black'):
                        if not(k == i and l == j):
                            count += 1
    return count
                

# Lancer le jeu
def launch():
    coords_cells_to_toggle = []
    print("")
    for i in range(size):
        print("")
        for j in range(size):
            # Si une cellule morte possède exactement
            # 3 cellules voisines vivantes, alors elle devient vivante
            if cells[i][j]["background"] == 'white':
                if alive_neighbours(i, j) == 3:
                    coords_cells_to_toggle.append((i,j))
            # Si une cellule vivante ne possède pas 2 ou 3 voisines
            # vivantes, alors elle meurt
            if cells[i][j]["background"] == 'black':
                if (alive_neighbours(i, j) < 2 or alive_neighbours(i, j) > 3):
                    coords_cells_to_toggle.append((i,j))
                    
    for coord_cell in coords_cells_to_toggle:
        toggle_bg(coord_cell[0], coord_cell[1])
        
# Réinitialise la grille
def reset():
    for i in range(size):
        for j in range(size):
            cells[i][j]["background"] = 'white'
            

# Création du bouton start
but_start = Button(fenetre, height = 2, borderwidth=3,
                   text = "Start",
                   command = launch)
but_start.grid(row = size, columnspan = 3, column = floor(size/2) - 2)

but_reset = Button(fenetre, height = 2, borderwidth=3,
                   text = "Reset",
                   command = reset)
but_reset.grid(row = size, columnspan = 3, column = floor(size/2) + 2)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

