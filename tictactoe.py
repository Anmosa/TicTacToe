"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    if any(None in row for row in board):
        XCount = sum(row.count("X") for row in board)
        OCount = sum(row.count("O") for row in board)

        if XCount == OCount:
            return "X"
        else:
            return "O"
    else:
        return
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    x = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x.add((i,j))
    return x


def result(board, actions):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = actions
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        playername = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = playername
        return new_board
    else:
        raise Exception("Invalid Actions")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    for i in range(3):
        if board[0][1] == board[1][i] == board[2][i] == "X":
            return "X"
        elif board[0][1] == board[1][i] == board[2][i] == "O":
            return "O"

    if board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return "X"
    if board[0][2] == board[1][1] == board[2][0] == "O":
        return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any(None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == "x":
        return 1
    elif 2 == "O":
        return -1
    else:
        return 0


def minimax(board):
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))    #FIXED
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))    #FIXED
            if k < v:
                v = k
                best_move = action
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v    #FIXED

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    #FIXED


# def minimax(board):
#     """
#     Returns the optimal actions for the current player on the board.
#     """
#     if terminal(board):
#         return None
#     if player(board) == "X":
#         best_val = -1
#         best_move = (-1,1)
#         c = sum(row.count(EMPTY) for row in board)
#         if c == 9:
#             return best_move
#         for actions in actions(board):
#             move_value = MIN_VALUE(result(board,actions))
#             if move_value == 1:
#                 best_move = actions
#                 break
#             if move_value > best_val:
#                 best_move = actions
#         return best_move
#     if player(board) == "O":
#         best_val = -1
#         best_move = (-1,1)
#         for actions in actions(board):
#             move_value = MAX_VALUE(result(board,actions))
#             if move_value == -1:
#                 best_move = actions
#                 break
#             if move_value < best_val:
#                 best_move = actions
#         return best_move

# def MIN_VALUE(board):
#     if terminal(board):
#         return utility(board)
#     v = 1
#     for actions in actions(board):
#         v = max(v, MAX_VALUE(result(board, actions)))
#         if v == 1:
#             break
#     return v

# def MAX_VALUE(board):
#     if terminal(board):
#         return utility(board)
#     v = -1
#     for actions in actions(board):
#         v = max(v, MIN_VALUE(result(board, actions)))
#         if v == 1:
#             break
#     return v