import numpy as np
from MySQLConn import cnx
BITMASK = 0b11111111111111111111111111111111
board = [
    0b11111111111100000000000000000000, # red piece 32 bit board
    0b00000000000000000000000000000000, # red king 32 bit board
    0b00000000000000000000111111111111, # black piece 32 bit board
    0b00000000000000000000000000000000  # black king 32 bit board
]
def initialize_game():
    db = cnx.cursor()
    ins_game_query = "INSERT INTO `Game` (winning_team) VALUES ('IN PROGRESS');"
    
    db.execute(ins_game_query)
    cnx.commit()

def training_data_into_DB(before_move, board, turn):
    turns_set = False
    if turn == 'R':
        if before_move[0] != board[0]:
            before_turn = before_move[0]
            after_turn  =  board[0]
            turns_set = True
        elif before_move[1] != board[1]:
            before_turn = before_move[1]
            after_turn  =  board[1]        
            turns_set = True
    elif turn == 'B':
        if before_move[2] != board[2]:
            before_turn = before_move[2]
            after_turn  =  board[2]
            turns_set = True
        elif before_move[3] != board[3]:
            before_turn = before_move[3]
            after_turn  =  board[3]        
            turns_set = True
    
    if (turns_set):
        db = cnx.cursor()
        ins_training_data_query = "INSERT INTO `training_data` (before_turn, after_turn, team) VALUES (%s, %s, '%s')" % (before_turn, after_turn, turn)
        
        db.execute(ins_training_data_query)
        cnx.commit()
    
        
def board_into_DB():
    db = cnx.cursor()
    db.execute("SELECT game_id FROM Game ORDER BY game_id DESC LIMIT 1;")
    game_id = db.fetchone()[0]

    ins_turn_query = """INSERT INTO `Turns` (game_id, red_piece_board, red_king_board, black_piece_board, black_king_board)
    VALUES (%s, %s, %s, %s, %s);""" % (game_id, board[0], board[1], board[2], board[3])
    
    db.execute(ins_turn_query)
    cnx.commit()

def make_move(piece_index, move_to_index, board_copy):
    
    # movement will of course be different as it is relative to starting position
    # next I am going to limit piece movement for border pieces by hard coding some border arrays and checking if piece_index in border_array:
    # if(piece_type == "RP" or piece_type == "RK"):
    #     if (move == "FR"):
    #         move_to_index = piece_index - 4
    #     elif(move == "FL"):
    #         move_to_index = piece_index - 6
    #     elif(move == "BR" and piece_type == "RK"):
    #         move_to_index = piece_index + 4
    #     elif(move == "FL" and piece_type == "RK"):
    #         move_to_index = piece_index + 6
    # elif(piece_type == "BP" or piece_type == "BK"):
    #     if (move == "FR"):
    #         move_to_index = piece_index + 4
    #     elif(move == "FL"):
    #         move_to_index = piece_index + 6
    #     elif(move == "BR" and piece_type == "BK"):
    #         move_to_index = piece_index - 4
    #     elif(move == "FL" and piece_type == "BK"):
    #         move_to_index = piece_index - 6
        
    if ((((board_copy[0] | board_copy[1] | board_copy[2] | board_copy[3]) ^ BITMASK) & (1<<move_to_index))):
        if (board_copy[0] & (1<<piece_index)):
            board_copy[0] ^= 1 << piece_index
            board_copy[0] ^= 1 << move_to_index
        if (board_copy[1] & (1<<piece_index)):
            board_copy[1] ^= 1 << piece_index
            board_copy[1] ^= 1 << move_to_index
        if (board_copy[2] & (1<<piece_index)):
            board_copy[2] ^= 1 << piece_index
            board_copy[2] ^= 1 << move_to_index
        if (board_copy[3] & (1<<piece_index)):
            board_copy[3] ^= 1 << piece_index
            board_copy[3] ^= 1 << move_to_index

        for i in range(4):
            if (board_copy[0] & (1<<i)):
                board_copy[0] ^= 1 << i
                board_copy[1] ^= 1 << i
        for i in range(28, 32):
            if (board_copy[2] & (1<<i)):
                board_copy[2] ^= 1 << i
                board_copy[3] ^= 1 << i

        return board_copy
    else:
        return 0

def print_board():
    positions = {}
    for i in range(32):
        if (board[0] & (1<<i)):
            positions["piece{0}".format(i)] = "RP"
        elif(board[1] & (1<<i)):
            positions["piece{0}".format(i)] = "RK"
        elif(board[2] & (1<<i)):
            positions["piece{0}".format(i)] = "BP"
        elif(board[3] & (1<<i)):
            positions["piece{0}".format(i)] = "BK"
        else:
            positions["piece{0}".format(i)] = "**"
            
    p00 = positions["piece0"]
    p01 = positions["piece1"]
    p02 = positions["piece2"]
    p03 = positions["piece3"]
    p04 = positions["piece4"]
    p05 = positions["piece5"]
    p06 = positions["piece6"]
    p07 = positions["piece7"]
    p08 = positions["piece8"]
    p09 = positions["piece9"]
    p10 = positions["piece10"]
    p11 = positions["piece11"]
    p12 = positions["piece12"]
    p13 = positions["piece13"]
    p14 = positions["piece14"]
    p15 = positions["piece15"]
    p16 = positions["piece16"]
    p17 = positions["piece17"]
    p18 = positions["piece18"]
    p19 = positions["piece19"]
    p20 = positions["piece20"]
    p21 = positions["piece21"]
    p22 = positions["piece22"]
    p23 = positions["piece23"]
    p24 = positions["piece24"]
    p25 = positions["piece25"]
    p26 = positions["piece26"]
    p27 = positions["piece27"]
    p28 = positions["piece28"]
    p29 = positions["piece29"]
    p30 = positions["piece30"]
    p31 = positions["piece31"]
    print(f'''
    -------------------------------------------------------------------------
    |        |31******|        |30******|        |29******|        |28******|
    |        |***{p31}***|        |***{p30}***|        |***{p29}***|        |***{p28}***|
    |        |********|        |********|        |********|        |********|
    |________|________|________|________|________|________|________|________|
    |27******|        |26******|        |25******|        |24******|        |
    |***{p27}***|        |***{p26}***|        |***{p25}***|        |***{p24}***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |23******|        |22******|        |21******|        |20******|
    |        |***{p23}***|        |***{p22}***|        |***{p21}***|        |***{p20}***|
    |        |********|        |********|        |********|        |********|
    |________|________|________|________|________|________|________|________|
    |19******|        |18******|        |17******|        |16******|        |
    |***{p19}***|        |***{p18}***|        |***{p17}***|        |***{p16}***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |15******|        |14******|        |13******|        |12******|
    |        |***{p15}***|        |***{p14}***|        |***{p13}***|        |***{p12}***|
    |        |********|        |********|        |********|        |********|
    |________|________|________|________|________|________|________|________|
    |11******|        |10******|        |09******|        |08******|        |
    |***{p11}***|        |***{p10}***|        |***{p09}***|        |***{p08}***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |07******|        |06******|        |05******|        |04******|
    |        |***{p07}***|        |***{p06}***|        |***{p05}***|        |***{p04}***| 
    |        |********|        |********|        |********|        |********|
    |________|________|________|________|________|________|________|________|
    |03******|        |02******|        |01******|        |00******|        |
    |***{p03}***|        |***{p02}***|        |***{p01}***|        |***{p00}***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    ''')

initialize_game()
print_board()
turn = 'R'
game_on = True
while game_on:
    before_move = board.copy()
    new_board = board.copy()
    piece_index = int(input("select a piece to move: "))
    input_move_to = int(input("select a location to move to: "))
    new_board = make_move(piece_index, input_move_to, new_board)
    if not new_board:
        print("Not a valid move!")
    else:
        board = new_board
        board_into_DB()
        if turn == 'R':
            training_data_into_DB(board, before_move, turn)
            turn = 'B'
        else:
            training_data_into_DB(board, before_move, turn)
            turn = 'R'
    print_board()
    game_on = True if ((board[0] | board[1]) or (board[2] | board[3])) else False
        







