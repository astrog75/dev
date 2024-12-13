import sys
import math

# Input processing for CG
# width, height = [int(i) for i in input().split()]
# board = [[0] * width for _ in range(height)]
# for i in range(height):
#     board.append(input())


# Input processing for local tests
board = ["2.X",
         "X.H",
         ".H1"]
width = 3
height = 3

balls_positions = []

for i in range(height):
    for j in range(height):
        if board[i][j].isdigit():
            balls_positions.append((i,j))

# directions = {'bottom': 'v', 
#               'left': '<', 
#               'right': '>', 
#               'up': '^'}

directions = [(-1,0), (0,1), (1,0), (0,-1)]

i = 0
while i < len(balls_positions):
    r, c = balls_positions[i]
    nb_shots = board[r][c]
    
    for d in directions:
        i, j = r + r*d[0], c + c*d[1]
        
        if 0 <= i <= h-1 and 0 <= j <= w-1:
            update_board()
            do the same thing with ball at position (i,j)
            
    
    if we find a way:
        i += 1
    else:
        i -= 1
    


def update_board()



    
    