from tkinter import *
from random import randint
from functools import partial

main = Tk()
main.title("Demineur")
main.geometry("300x300+500+300")

n_lines = 10
n_columns = 10

# probabilité qu'une cellule soit minée
p = 0.1

color = ["blue", "green", "red", "purple", "magenta", "maroon", "lime", "black"]

# Place une mine dans une cellule avec une probabilité p
# Retourne 1 si la cellule est minée
def place_mine(p):
    n = randint(1, 10000)
    if n < p*10000:
        return 1
    else:
        return 0

##def mines_voisines(i, j):
##    # Gestion des bords
##    count = 0
##    # Gestion des bords
##    if (i == 0): # 1ere ligne
##        if (j == 0): # Coin supérieur gauche
##            count = 0
##            if (cells[0][1] == 1):
##                count += 1
##            if (cells[1][0] == 1):
##                count += 1
##            if (cells[1][1] == 1):
##                count += 1
##        elif (j == n_columns-1): # Coin supérieur droit
##            count = 0
##            if (cells[0][j-1] == 1):
##                count += 1
##            if (cells[1][j-1] == 1):
##                count += 1
##            if (cells[1][j] == 1):
##                count += 1
##        else: # On est sur la 1ere ligne, mais pas dans les coins
##            count = 0
##            if (cells[0][j-1] == 1):
##                count += 1
##            if (cells[1][j-1] == 1):
##                count += 1
##            if (cells[1][j] == 1):
##                count += 1
##            if (cells[1][j+1] == 1):
##                count += 1
##            if (cells[0][j+1] == 1):
##                count += 1
##    if (i == n_lines-1): # dernière ligne
##        if (j == 0): # Coin inférieur gauche
##            count = 0
##            if (cells[i-1][0] == 1):
##                count += 1
##            if (cells[i-1][1] == 1):
##                count += 1
##            if (cells[i][1] == 1):
##                count += 1
##        elif (j == n_columns-1): # Coin inférieur droit
##            count = 0
##            if (cells[i-1][j] == 1):
##                count += 1
##            if (cells[i-1][j-1] == 1):
##                count += 1
##            if (cells[i][j-1] == 1):
##                count += 1
##        else: # On est sur la dernière ligne, mais pas dans les coins
##            count = 0
##            if (cells[i][j-1] == 1):
##                count += 1
##            if (cells[i-1][j-1] == 1):
##                count += 1
##            if (cells[i-1][j] == 1):
##                count += 1
##            if (cells[i-1][j+1] == 1):
##                count += 1
##            if (cells[i][j+1] == 1):
##                count += 1
##    else:
##        if (j == 0):
##            count = 0
##            if (cells[i-1][0] == 1):
##                count += 1
##            if (cells[i-1][1] == 1):
##                count += 1
##            if (cells[i][1] == 1):
##                count += 1
##            if (cells[i+1][1] == 1):
##                count += 1
##            if (cells[i+1][0] == 1):
##                count += 1
##        elif (j == n_columns-1):
##            count = 0
##            if (cells[i-1][j] == 1):
##                count += 1
##            if (cells[i-1][j-1] == 1):
##                count += 1
##            if (cells[i][j-1] == 1):
##                count += 1
##            if (cells[i+1][j-1] == 1):
##                count += 1
##            if (cells[i+1][j] == 1):
##                count += 1
##        else: # Cas général
##            count = 0
##            for k in range(i-1, i+2):
##                for l in range(j-1, j+2):
##                    if (cells[k][l] == 1):
##                        if not(k == i and l == j):
##                            count += 1
##    return count

    
def mines_voisines(i, j):
    count = 0
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if (cells[k][l] == 1):
                if not(k == i and l == j):
                    count += 1
    return count
 

def state(i, j, event):
    if cells[i][j] == 1:
        print("Perdu !!")
        reveal_all()
    else:
        if gagnee() == 1:
            print("gagné !")
        else:
            mines = mines_voisines(i, j)
            cells_state[i][j] = 1
            
            cells_to_unveil = [] # Liste de coordonnées de cellules
            cells_to_unveil.append((i, j))
            while (len(cells_to_unveil) != 0):
                print(len(cells_to_unveil))
                for cell in cells_to_unveil:
                    i = cell[0]
                    j = cell[1]
                    cells_to_unveil.remove((i, j))
                    mines = mines_voisines(i, j)
                    cells_state[i][j] = 1
                    if mines > 0:
                        buttons[i][j]["text"] = str(mines)
                        buttons[i][j]["foreground"] = color[mines-1]
                        buttons[i][j]["background"] = "white"
                        buttons[i][j]["relief"] = "sunken"
                    else:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                if cells_state[k][l] == 0:
                                    if cells[k][l] == 0:
                                        cells_to_unveil.append((k, l))
                                        buttons[k][l]["background"] = "white"
                                        #print(len(cells_to_unveil))


# Une partie est gagnée si toutes les cellules sont dévoilées et toutes les mines sont marquées
def gagnee():
    for i in range(1, n_lines):
        for j in range(1, n_columns):
            if cells_state[i][j] < 2:
                return 0
            else:
                if cells_state[i][j] == 2 and cells[i][j] != 1:
                    return 0
    return 1


def reveal_all():
    for i in range(n_lines + 1):
        for j in range(n_columns + 1):
            if cells[i][j] == 1:
                buttons[i][j]["background"] = "red"

                        
def flag(i, j, event):
    # On marque la cellule comme déminée
    if cells[i][j] != 3:
        if cells[i][j] != 2:
            cells[i][j] = 2
            buttons[i][j]["background"] = "red"
        else:
            buttons[i][j]["background"] = "gray"


# Le tableau est composée de cellules
# à 4 états :
# 0 cachée, non minée
# 1 cachée, minée
# 2 cachée flaguée comme minée
# 3 révélée
cells = [] 
buttons = []
for i in range(n_lines + 2):
    cells.append([0]* (n_columns + 2))
    buttons.append([[]] * (n_columns + 2))

# Construction du plateau de jeu 
for i in range(1, n_lines + 1):
    for j in range(1, n_columns + 1):
        buttons[i][j] = Button(main, width = 1, height = 1,
                               relief = "groove", background = "gray")
        buttons[i][j].grid(row = i, column = j)
        buttons[i][j].bind("<Button-1>", partial(state, i, j))
        buttons[i][j].bind("<Button-3>", partial(flag, i, j))
        
        cells[i][j] = place_mine(p)

main.mainloop()
