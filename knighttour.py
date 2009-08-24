# http://en.wikipedia.org/wiki/Knight%27s_tour#In_Python

from random import random
from operator import itemgetter
 
NMOVES = 8
BOARD_SIZE = 8

moves = ((2,1), (2,-1), (1,2), (1,-2), (-1,2),
         (-1,-2), (-2,1), (-2,-1))
 
# creates a BOARD_SIZE * BOARD_SIZE matrix of integer zeros
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def in_range_and_empty(posx, posy):
    return ((0 <= posx < BOARD_SIZE)  and
            (0 <= posy < BOARD_SIZE) and
             board[posx][posy] == 0)

def get_accessibility(x, y):
    return sum(1 for deltax, deltay in moves if in_range_and_empty(x + deltax, y + deltay))

def moves_from(positionx, positiony):
    for deltax, deltay in moves:
        yield positionx + deltax, positiony + deltay

def get_next_moves(move):
    positionx, positiony = move
    all_possible_moves = [((newx, newy), get_accessibility(newx, newy)) for newx, newy in moves_from(positionx, positiony) if in_range_and_empty(newx, newy)]
    if len(all_possible_moves) == 0:
        print_board()
        assert(len(all_possible_moves) > 0)
    best_move = sorted(all_possible_moves, key=itemgetter(1))[0]
    return best_move[0]

def start_pos():
    return int(random() * BOARD_SIZE), int(random() * BOARD_SIZE)

def print_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print "%4d" % board[i][j],
        print
    
def main():
    positionx, positiony = start_pos()
    board[positionx][positiony] = 1 # first move
 
    # compute moves
    for move_number in range(2, BOARD_SIZE * BOARD_SIZE + 1):
        move = positionx, positiony
        positionx, positiony = get_next_moves(move)
        board[positionx][positiony] = move_number
 
    print_board()

main()
