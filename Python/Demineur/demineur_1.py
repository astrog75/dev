# Classe cell, gérant une case du jeu de mine
# Attributs : minée ou pas; flaguée ou pas
# méthodes : 

class Cell:
    mine = 0
    flag = 0

# Classe gérant un champ de mines
class Field:
    n_lines = 10
    n_columns = 10
    field = Cell[n_lines][n_columns]

    def __init__(self):
        
    
# Classe Game, gérant l'éxecution d'une partie
class Game:
    
