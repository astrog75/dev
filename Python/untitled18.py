# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:48:11 2023

@author: moty_
"""

def numRookCaptures(board):

        size_board = 8
        row_rook = 0
        col_rook = 0
        for i in range(size_board):
            for j in range(size_board):
                #print(board[i][j])
                if board[i][j] == 'R':
                    #print("test")
                    row_rook = i
                    col_rook = j
                    break
        
        nb_attacked_pieces = 0
        for i in range(row_rook-1, -1, -1):
            if board[i][col_rook] != '.':
                if board[i][col_rook] == 'p':
                    nb_attacked_pieces += 1
                break
        
        for i in range(row_rook+1, size_board):
            if board[i][col_rook] != '.':
                if board[i][col_rook] == 'p':
                    nb_attacked_pieces += 1
                break
        
        for j in range(col_rook-1, -1, -1):
            if board[row_rook][j] != '.':
                if board[row_rook][j] == 'p':
                    nb_attacked_pieces += 1
                    break
        
        for j in range(col_rook+1, size_board):
            if board[row_rook][j] != '.':
                if board[row_rook][j] == 'p':
                    nb_attacked_pieces += 1
                    break
        
        return nb_attacked_pieces

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(numRookCaptures(board))