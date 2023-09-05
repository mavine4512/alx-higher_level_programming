#!/usr/bin/python3
'''Solves the N-queens puzzle
'''

import sys


def init_board(n):
    '''Initialize an `n`x`n` sized chessboard with 0's.
    '''
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    '''Return a deepcopy of a chessboard.
    '''
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

def get_solution(board):
    '''Return the list of lists representation of a solved chessboard.
    '''
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)

def xout(board, row, col):
    '''X out spots on a chessboard.
    All spots where non_attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    '''
    for c in range(col + 1, len(board)):
        board[row][c] = "x"

    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    for r in range(row + 1, len(board)):
        board[r][col] = "x"

    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    c = col + 1
