import bitboard as bb
import datetime as dt
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
    ins_game_query = "INSERT INTO `Game` (winning_team, CREATE_DATE) VALUES ('IN PROGRESS', '{}');".format(dt.datetime.now())
    
    db.execute(ins_game_query)
    cnx.commit()

def game_results_into_DB(winner):
    db = cnx.cursor()
    db.execute("SELECT game_id FROM Game ORDER BY game_id DESC LIMIT 1;")
    game_id = db.fetchone()[0]

    db = cnx.cursor()
    update_game_query = "UPDATE `Game` SET winning_team = '{}' WHERE game_id = {};".format(winner, game_id)
    
    db.execute(update_game_query)
    cnx.commit()

def training_data_into_DB(before_move, board, player, round_num):
    king_move = False
    piece_move = False
    if player == 'R':
        if before_move[0] != board[0]:
            before_turn = before_move[0]
            after_turn  =  board[0]
            piece_move = True
        elif before_move[1] != board[1]:
            before_turn = before_move[1]
            after_turn  =  board[1]        
            king_move = True
    elif player == 'B':
        if before_move[2] != board[2]:
            before_turn = before_move[2]
            after_turn  =  board[2]
            piece_move = True
        elif before_move[3] != board[3]:
            before_turn = before_move[3]
            after_turn  =  board[3]        
            king_move = True
    
    if (piece_move):
        db = cnx.cursor()
        ins_training_data_query = "INSERT INTO `piece_training_data` (before_turn, after_turn, team) VALUES ({}, {}, '{}')".format(before_turn, after_turn, player)
        
        db.execute(ins_training_data_query)
        cnx.commit()
    elif (king_move):
        db = cnx.cursor()
        ins_training_data_query = "INSERT INTO `king_training_data` (before_turn, after_turn, team) VALUES ({}, {}, '{}')".format(before_turn, after_turn, player)
        
        db.execute(ins_training_data_query)
        cnx.commit()
    
    # get the current match assuming im the only one playing and there arent concurrent games going on
    db = cnx.cursor()
    db.execute("SELECT game_id FROM Game ORDER BY game_id DESC LIMIT 1;")
    game_id = db.fetchone()[0]

    if player == 'R':
        ins_turn_query = """INSERT INTO `Turns` (game_id, round_num, before_rp_board, before_rk_board, before_bp_board, before_bk_board)
        VALUES ({}, {}, {}, {}, {}, {});""".format(game_id, round_num, board[0], board[1], board[2], board[3])
        
        db.execute(ins_turn_query)
        cnx.commit()
    elif player == 'B':
        ins_turn_query = """UPDATE `Turns` 
        SET
        after_rp_board = {}, 
        after_rk_board = {}, 
        after_bp_board = {}, 
        after_bk_board = {}
        WHERE game_id = {} AND round_num = {};
        """.format(board[0], board[1], board[2], board[3], round_num, game_id,)
        
        db.execute(ins_turn_query)
        cnx.commit()

def make_move(piece_index, move_to_index, board_copy):
        
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
        # next we have a block of rules to check
        # if piece_index in one of the king boards:
            # is_king = True
        # else:
            # is_king = False
        is_king = True
        odd_rows = [0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27]
        even_rows = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
        if is_king: # will write in more logic for extra moves king can do
            print("woooooo im the king!!!")
        else:
            if piece_index in odd_rows:
                if move_to_index == ((piece_index + 4) or (piece_index + 5)):
                    pass
                elif move_to_index == ((piece_index + 7) or (piece_index + 9)):
                    print("more conditions to write here")
                    if True: # 
                        pass
                    else:
                        return board_copy
            elif piece_index in even_rows:
                if move_to_index == ((piece_index + 4) or (piece_index + 5)):
                    pass
                elif move_to_index == ((piece_index + 7) or (piece_index + 9)):
                    print("more conditions to write here")
                    if True:
                        pass
                    else:
                        return board_copy
            print("the conditions for if not king go here")
        # king me below
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

initialize_game()
bb.print_board(board)
player = 'R'
round_num = 1
game_on = True
while game_on:
    before_move = board.copy()
    new_board = board.copy()
    piece_index = int(input("select a piece to move: "))
    input_move_to = int(input("select a location to move to: "))
    new_board = make_move(piece_index, input_move_to, new_board)
    if not new_board:
        print("Not a valid move, try again!")
    else:
        board = new_board
        training_data_into_DB(board, before_move, player, round_num)
        player = 'R' if player == 'B' else 'B'
        round_num += 1 if player == 'R' else 0 # we only want to increment the round num after both teams have gone

    bb.print_board(board)
    game_on = True if ((board[0] or board[1]) and (board[2] or board[3])) else False # if one side or the other is 0, game over

if not game_on:
    winner = 'R' if (board[0] or board[1]) else 'B' # game is over, insert winning into db
    game_results_into_DB(winner)
        







