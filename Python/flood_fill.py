# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:49:11 2024

@author: moty_
"""

from collections import deque

# Display the grid
def print_board(board):
    for row in board:
        print(''.join(row))
    print()

# Test 1 in CG
# w = 10
# h = 10
# board = [list("..#.#...##"),
#           list("#..#.#...."),
#           list(".........#"),
#           list("..#..#..#."),
#           list(".......#.."),
#           list("..#.JJDI.#"),
#           list("..#.....#."),
#           list(".....#..#."),
#           list(".........."),
#           list("..........")]

# Test 4 in CG
board = [
list("....#...........KYLO...#."),
list("#.....#...#..#........#.#"),
list("..REY..........#..#......"),
list("#...#..#.#........##.#.#."),
list("..#............#........."),
list("......#.........#......#."),
list(".#........#........#...#."),
list("#..HAN..................."),
list("......#....#.##.....##.#."),
list("##..#....#.#....#..#....."),
list("..............###......#."),
list("#.....#.........#...##..."),
list("...##..##.......#........"),
list(".#.###..#.....#.#.....#.#"),
list("....#...FN2187.....#....."),
list("..#.........#....#.#....."),
list("...........#...#.#...#..."),
list(".#...##...##.....#..#..#."),
list("..................#...##."),
list(".....#.#....##.......#..#"),
list("..........#........#.#..."),
list(".#.............#......#.#"),
list("...#.#.#.###..#..#.....##"),
list("#.#........###.......#..."),
list("..##.LEIA......#..#.##.##")]
w = 25
h = 25

print_board(board)

# To paste to CG editor
# for i in range(h):
#     line = input()
#     board.append(list(line))
#     for j, c in enumerate(line):
#         if c not in "#.":
#             tower_positions[c] = (i,j)

towers_positions = []
towers_distance = {}
towers_name = []

for i in range(h):
    for j in range(w):
        if board[i][j] not in "#.":
            towers_distance[(i,j)] = 0
            towers_positions.append((i,j))
            towers_name.append(board[i][j])

# Handle the case where 2 towers have the same name - Version 1
M = max(towers_name)
seen = set()
towers_name = {}
k = 1

for i in range(h):
    for j in range(w):
        if board[i][j] not in "#.":
            curr = board[i][j]
            if curr not in seen:
                seen.add(curr)
                towers_name[curr] = curr
            else:
                new_name = chr(ord(M)+k)
                towers_name[new_name] = curr
                board[i][j] = new_name
                k += 1

# Handle the case where 2 towers have the same name - Version 2
# towers_name = []
# for i, tower in enumerate(towers_positions):
#     r, c = tower[0], tower[1]
#     board[r][c] = str(i)
#     towers_name.append(str(i))

print_board(board)
print(towers_name)

# Preparing for main Loop
stack = deque()

directions = [(-1,0), (0,1), (1,0), (0,-1)]

for tower_pos in towers_positions:
    stack.append(tower_pos)

gen = 0
sub_gen = len(stack)

# Main Loop
while stack:
    
    curr_position = stack.popleft()
        
    i, j = curr_position[0], curr_position[1]
    curr_tower = board[i][j]
    
    for d in directions:
        
        r, c = i + d[0], j + d[1]
        
        if 0 <= r <= h-1 and 0 <= c <= w-1:
            
            if board[r][c] == '.':
                board[r][c] = curr_tower
                towers_distance[(r,c)] = towers_distance[(i,j)] + 1
                stack.append((r,c))
            elif board[r][c] in towers_name:
                if board[r][c] != board[i][j]:
                    if towers_distance[(r,c)] == towers_distance[(i,j)] + 1:
                        board[r][c] = '+'
    
    sub_gen -= 1
    if sub_gen == 0:
        gen += 1
        print("generation :", gen)
        print_board(board)
        sub_gen = len(stack)

# Back to the original tower names
for i in range(h):
    for j in range(w):
        if board[i][j] in towers_name:
            board[i][j] = towers_name[board[i][j]]

print_board(board)