# TETRIS
# To do :
# Gérer conditions aux limites des déplacements
# Gérer taille des pieces (notamment piece en L)


from tkinter import *
from random import randint

# Constantes
# width et height doivent être des multiples de size_bloc
size_bloc = 45 # Taille d'un seul bloc
width = 450
height = 720

if width % size_bloc == 0:
    n_columns = width//size_bloc
else:
    print("Erreur de dimensions")

if height % size_bloc == 0:
    n_lines = height//size_bloc
else:
    print("Erreur de dimensions")

# Fenetre principale et plateau de jeu
root = Tk()
root.title("Tetris")

nb_lines = Label(root, text = "lignes réussies : ")
nb_lines.pack(side = LEFT)

playgd = Canvas(root, width = width, height = height, background = "black")
playgd.pack(side = LEFT)

# On découpe le tableau de jeu en cubes
# Possèdant 2 états : 0 (libre) ou 1 (occupée)         
cells = []
for i in range(n_lines):
    current_line = []
    for j in range(n_columns):
        current_line.append("libre")
    cells.append(current_line)

# Test
##for i in range(n_lines):
##    for j in range(n_columns):
##        print(cells[i][j], end = ' ')
##    print()

        
# Création des différentes pièces
# Bloc 2*2
# Remarque : construit la pièce mais ne la dessine pas
piece_bloc = Canvas(playgd)
bloc1 = Canvas(piece_bloc, bg = "red")
bloc1.place(x = 0, y = 0, width = size_bloc, height = size_bloc)
bloc2 = Canvas(piece_bloc, bg = "red")
bloc2.place(x = 0, y = size_bloc, width = size_bloc, height = size_bloc)
bloc3 = Canvas(piece_bloc, bg = "red")
bloc3.place(x = size_bloc, y = 45, width = size_bloc, height = size_bloc)
bloc4 = Canvas(piece_bloc, bg = "red")
bloc4.place(x = size_bloc, y = 0, width = size_bloc, height = size_bloc)

# Piece 4*1
# Remarque : construit la pièce mais ne la dessine pas
piece_41 = Canvas(playgd)
bloc1 = Canvas(piece_41, bg = "blue")
bloc1.place(x = 0, y = 0, width = size_bloc, height = size_bloc)
bloc2 = Canvas(piece_41, bg = "blue")
bloc2.place(x = 0, y = size_bloc, width = size_bloc, height = size_bloc)
bloc3 = Canvas(piece_41, bg = "blue")
bloc3.place(x = 0, y = 2*size_bloc, width = size_bloc, height = size_bloc)
bloc4 = Canvas(piece_41, bg = "blue")
bloc4.place(x = 0, y = 3*size_bloc, width = size_bloc, height = size_bloc)

# Piece "en L"
# Remarque : construit la pièce mais ne la dessine pas
piece_L = Canvas(playgd)
bloc1 = Canvas(piece_L, bg = "green")
bloc1.place(x = 0, y = 0, width = size_bloc, height = size_bloc)
bloc2 = Canvas(piece_L, bg = "green")
bloc2.place(x = 0, y = size_bloc, width = size_bloc, height = size_bloc)
bloc3 = Canvas(piece_L, bg = "green")
bloc3.place(x = 0, y = 2*size_bloc, width = size_bloc, height = size_bloc)
bloc4 = Canvas(piece_L, bg = "green")
bloc4.place(x = size_bloc, y = 2*size_bloc, width = size_bloc, height = size_bloc)

# Liste des pièces du jeu
liste_pieces = [piece_bloc, piece_41, piece_L]

def droite(piece, event):
    x_bloc = int(piece.place_info()['x'])
    y_bloc = int(piece.place_info()['y'])

    line = y_bloc//size_bloc
    column = x_bloc//size_bloc

    # Cas si la pièce est un bloc
    if x_bloc < (width - 2*size_bloc): #Si la piece n'est pas déjà complètement à droite
        if cells[line][column+1] == "libre" and cells[line+1][column+1]== "libre":
            piece.place(x = x_bloc + size_bloc, y = y_bloc)

def gauche(piece, event):
    x_bloc = int(piece.place_info()['x'])
    y_bloc = int(piece.place_info()['y'])
    
    if x_bloc > 0:
        piece.place(x = x_bloc - size_bloc, y = y_bloc)

def bas(piece, event):
    x_bloc = int(piece.place_info()['x'])
    y_bloc = int(piece.place_info()['y'])
    
    if y_bloc < height - 2*size_bloc:
        piece.place(x = x_bloc, y = y_bloc + size_bloc)

# Tire la prochaine pièce au hasard parmi les 5 pièces
def choose_piece():
    n = randint(0, 2)
    return liste_pieces[n]

def start_game():
    
    # To do here : Appel à reset pour réinitialiser le tableau de jeu
    #reset()
    #etat_jeu()
    cells[0][8] = "occupée"
    etat_jeu()
    
    # Choix de la prochaine piece
    current_piece = choose_piece()

    # Affichage de la prchaine piece sur la ligne du haut, au milieu
    if current_piece == piece_bloc:
        current_piece.place(x = width/2 , y = 0, width = 2*size_bloc, height = 2*size_bloc)
    elif current_piece == piece_41:
        current_piece.place(x = width/2 , y = 0, width = size_bloc, height = 4*size_bloc)
    elif current_piece == piece_L:
        current_piece.place(x = width/2, y = 0, width = 2*size_bloc, height = 3*size_bloc)
        
    root.bind("<Right>", lambda piece = current_piece:droite(current_piece, "<Right>"))
    root.bind("<Left>", lambda piece = current_piece:gauche(current_piece, "<Left>"))
    root.bind("<Down>", lambda piece = current_piece:bas(current_piece, "<Down>"))

def reset():
    global cells
    global playgd
    
    playgd["background"] == "yellow"
    
    for i in range(n_lines):
        for j in range(n_columns):
            cells[i][j] == "libre"
            
def etat_jeu():
    for i in range(n_lines):
        for j in range(n_columns):
            print(cells[i][j], end = ' ')
        print()
    print()
    

# Buttons
but_start = Button(root, height = 2, borderwidth=3,
                   text = "Start",
                   command = start_game)
but_start.pack(side = LEFT)

but_reset = Button(root, height = 2, borderwidth=3,
                   text = "Reset",
                   command = reset)
but_start.pack(side = LEFT)

but_quit = Button(root, height = 2, borderwidth=3,
                   text = "Quit",
                   command = root.destroy)
but_start.pack(side = LEFT)

root.mainloop()
