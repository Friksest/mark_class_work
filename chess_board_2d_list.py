from os import system
system("clear")
## CHESS BOARD + PIECES 

#   * list 2d list / matrix 
#   * loops and conditionals
#   * algorithms

SIZE = (8,8) # tuple

EMPTY   = 0

WKING   = 1
WQUEEN  = 2
WBISHOP = 3
WKNIGHT = 4
WROOK   = 5
WPAWN   = 6

BKING   = 11
BQUEEN  = 12
BBISHOP = 13
BKNIGHT = 14
BROOK   = 15
BPAWN   = 16

pieces = " ♚♛♝♞♜♟    ♔♕♗♘♖♙"
pieces_codes = [" ", "wk", "wq", "wb", "wn", "wr", "wp", " ", " ", " ", " ", "bk", "bq", "bb", "bn", "br", "bp"] # HW3: coplite black list
score_codes =  [" ",    0,    9,    3,    3,    5,    1, " ", " ", " ", " ",    0,    9,    3,    3,    5,    1] # HW3: coplite black list




wscore = 0
 
# list 2d
board = [
    [ 5,  4,  3,  1,  2,  3,  4,  5],
    [ 6,  6,  6,  0,  6,  6,  6,  6],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  6,  0,  0,  0,  0],
    [16, 16, 16, 16, 16, 16, 16, 16],
    [15, 14, 13, 11, 12, 13, 14, 15],
]

alphabet = "abcdefgh"
####################### PRINT BOARD ##################
game_over = False
while not game_over:
    
    #################################
    # HW2: add column coordinates on board TOP 
    #      a,b,c,//
    #  HERE <
    #       for
    
    system("clear")
    print(" ", end=" ")
    for c in alphabet:
        print(f"{c:^5}", end="")
    print()

    for ri in range(SIZE[0]):
        print(" " + "-----" * SIZE[1] + "-")
        rc = SIZE[0] - ri
        # ROW
        print(rc, end="")
        for ci in range(SIZE[1]):
            piece = pieces[board[ri][ci]]
            #if board[ri][ci] == BKING:
            #    piece = " ♚"
            #elif board[ri][ci] == BQUEEN:
            #    piece = " ♛"
            #elif board[ri][ci] == BBISHOP:
            #    piece = " ♝"
            #elif board[ri][ci] == BKNIGHT:
            #    piece = " ♞"
            #elif board[ri][ci] == BROOK:
            #    piece = " ♜"
            #elif board[ri][ci] == BPAWN:
            #    piece = " ♟"
            print(f"|{piece:^4}", end ="")
        print("|")
        # ROW

    print(" " + "-----" * SIZE[1] + "-")
####################### PRINT BOARD ##################

####################### INTERECTION ##################
    print(f"White score is:", wscore)
    move = input("Your move > ") 
    what, from_, to_ = move[0:2], move[2:4], move[4:6]
    print(what, from_, to_ )
    
    if what not in pieces_codes:
        print("wrong piece code!!!")
    else:
        pieces_code = pieces_codes.index(what)
        ci_from = alphabet.index(from_[0])
        ri_from = SIZE[0] - int(from_[1])

        ri_to   = SIZE[0] -  int(to_[1])
        ci_to   = alphabet.index(to_[0])
        #print(pieces_code, ri_from, ci_from)
        #print(pieces_code, ri_to, ci_to)

        if board[ri_from][ci_from] == pieces_code:
            if pieces_code == WPAWN:
                if ci_from == ci_to:
                    if ri_from == 1 and ri_to - 2 or ri_from == ri_to -1:
                        if board[ri_to][ci_to] == EMPTY:
                            board[ri_from][ci_from] = EMPTY
                            board[ri_to][ci_to] = pieces_code
                #####  1.checked left/right diagonal + move on it + incr score ######           
                else:
                    if ci_to == ci_from - 1 or ci_from +1:                
                        if board[ri_to][ci_to] != EMPTY and ri_to != ri_from:
                            wscore += score_codes[board[ri_to][ci_to]] # score per piece
                            board[ri_from][ci_from] = EMPTY
                            board[ri_to][ci_to] = pieces_code                            
                ##### /1.checked left/right diagonal + move on it + incr score ######           

            
                # else if  ... : HW4
                # wright conditions to:
                # 1. check left right diagonal 
                # 2. if there is a piece - move on it
                # 3. increase score by corresponding value (chess.com)
        else:
            print("The piece you try to move is not there!")
    input()
####################### INTERECTION ##################




# HW1*:  Try to use UTF8 - box drawing. 







# MOVMENT CHESS NOTATION PROTOCOL 
#   <piece>-<from>-<to>
#   wpd7d6