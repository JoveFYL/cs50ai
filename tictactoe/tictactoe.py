"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math
from tkinter import W

X = "X"
O = "O"
EMPTY = None
WINNING_COMBINATIONS = [
    {(0, 0), (0, 1), (0, 2)},
    {(1, 0), (1, 1), (1, 2)},
    {(2, 0), (2, 1), (2, 2)},
    {(0, 0), (1, 0), (2, 0)},
    {(0, 1), (1, 1), (2, 1)},
    {(0, 2), (1, 2), (2, 2)},
    {(0, 0), (1, 1), (2, 2)},
    {(0, 2), (1, 1), (2, 0)}
]


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = sum(x is not EMPTY for row in board for x in row)
    return X if count % 2 == 0 else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_positions = {(row, col) 
               for row in range(len(board)) 
               for col in range(len(board[row])) 
               if board[row][col] == EMPTY} 
    
    return empty_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    copy = deepcopy(board)
    if action not in possible_actions:
        raise Exception('Action not allowed!')

    curr_player = player(board)
    copy[action[0]][action[1]] = curr_player

    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_positions = {(row, col) 
               for row in range(len(board)) 
               for col in range(len(board[row])) 
               if board[row][col] == X}

    o_positions = {(row, col) 
               for row in range(len(board)) 
               for col in range(len(board[row])) 
               if board[row][col] == O}

    for combination in WINNING_COMBINATIONS:
        if combination.issubset(x_positions):
            return X
        if combination.issubset(o_positions):
            return O
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    
    empty_count = sum(x is EMPTY for row in board for x in row)    
    if empty_count == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
        
    # find current player
    curr_player = player(board)

    # if X, MAX player
    if curr_player == X:
        best_val = -math.inf
        best_action = None
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_action = action
        return best_action

    # else MIN player
    else:
        if curr_player == O:
            best_val = math.inf
            best_action = None
            for action in actions(board):
                val = max_value(result(board, action))
                if val < best_val:
                    best_val = val
                    best_action = action
            return best_action
    
    
def min_value(board):
    """
    Returns the minimum value for the MIN player.
    """
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    """
    Returns the maximum value for the MAX player.
    """
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

