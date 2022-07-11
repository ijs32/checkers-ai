from shutil import move
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

def training_data_into_DB(before_move, board, player, round_num, points):
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
        ins_training_data_query = """INSERT INTO `piece_training_data` (before_turn, after_turn, team, points) VALUES 
        ({}, {}, '{}', {})""".format(before_turn, after_turn, player, points)
        
        db.execute(ins_training_data_query)
        cnx.commit()
    
    elif (king_move):
        db = cnx.cursor()
        ins_training_data_query = """INSERT INTO `king_training_data` (before_turn, after_turn, team, points) VALUES 
        ({}, {}, '{}', {})""".format(before_turn, after_turn, player, points)
        
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
        upd_turn_query = """UPDATE `Turns` 
        SET
        after_rp_board = {}, 
        after_rk_board = {}, 
        after_bp_board = {}, 
        after_bk_board = {}
        WHERE game_id = {} AND round_num = {};
        """.format(board[0], board[1], board[2], board[3], game_id, round_num)
        
        db.execute(upd_turn_query)
        cnx.commit()

def make_move(piece_index, move_to_index, board_copy, player):
    points = 0

    if player == 'R':
        if ((board_copy[0] | board_copy[1]) & (1<<piece_index)): 
            is_king = False if (board_copy[0] & (1<<piece_index)) else True
            pass # this block checks that you selected a square with a piece to move on Red
        else:
            print("no piece selected Red")
            return False, 0
    elif player == 'B':
        if ((board_copy[2] | board_copy[3]) & (1<<piece_index)):
            is_king = False if (board_copy[2] & (1<<piece_index)) else True
            pass # this block checks that you selected a square with a piece to move on black
        else:
            print("no piece selected Black")
            return False, 0

    if ((((board_copy[0] | board_copy[1] | board_copy[2] | board_copy[3]) ^ BITMASK) & (1<<move_to_index))): 
        pass
    else:
        print("piece occupying area moved to")
        return False, 0

    odd_rows = [0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27]
    even_rows = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
    left_border = [3,11,19,27]
    left_border_moves = [piece_index + 4, piece_index - 4, piece_index + 9, piece_index - 9]
    right_border = [4,12,20,28]
    right_border_moves = [piece_index + 4, piece_index - 4, piece_index + 7, piece_index - 7]
    if piece_index in left_border:
        if move_to_index in left_border_moves:
            pass
        else:
            print("left border piece")
            return False, 0
    elif piece_index in right_border:
        if move_to_index in right_border_moves:
            pass
        else:
            print("right border piece")
            return False, 0
    # GIANT BLOCK OF CONDITIONALS BELOW, AVERT YOUR EYES
    if is_king:
        king_jumps = [piece_index+7, piece_index+9, piece_index-7, piece_index-9]
        even_king_moves = [piece_index+4, piece_index+3, piece_index-4, piece_index-5]
        odd_king_moves = [piece_index+5, piece_index+4, piece_index-3, piece_index-4]
        if (move_to_index in odd_king_moves and piece_index in odd_rows):
            pass
        elif (move_to_index in even_king_moves and piece_index in even_rows):
            pass
        elif move_to_index in king_jumps:
            opposite_teams_pieces = even_king_moves if (piece_index in even_rows) else odd_king_moves
            if player == 'R':
                if ((move_to_index == piece_index + 9) and ((board_copy[2] | board_copy[3]) & (1<<opposite_teams_pieces[0]))):
                    if ((board_copy[2]) & (1<<opposite_teams_pieces[0])):
                        board_copy[2] ^= 1<<opposite_teams_pieces[0]
                        points += 1
                    elif ((board_copy[3]) & (1<<opposite_teams_pieces[0])):
                        board_copy[3] ^= 1<<opposite_teams_pieces[0]
                        points += 1
                elif ((move_to_index == piece_index + 7) and ((board_copy[2] | board_copy[3]) & (1<<opposite_teams_pieces[1]))):
                    if ((board_copy[2]) & (1<<opposite_teams_pieces[1])):
                        board_copy[2] ^= 1<<opposite_teams_pieces[1]
                        points += 1
                    elif ((board_copy[3]) & (1<<opposite_teams_pieces[1])):
                        board_copy[3] ^= 1<<opposite_teams_pieces[1]
                        points += 1
                elif ((move_to_index == piece_index - 7) and ((board_copy[2] | board_copy[3]) & (1<<opposite_teams_pieces[2]))):
                    if ((board_copy[2]) & (1<<opposite_teams_pieces[2])):
                        board_copy[2] ^= 1<<opposite_teams_pieces[2]
                        points += 1
                    elif ((board_copy[3]) & (1<<opposite_teams_pieces[2])):
                        board_copy[3] ^= 1<<opposite_teams_pieces[2]
                        points += 1
                elif ((move_to_index == piece_index - 9) and ((board_copy[2] | board_copy[3]) & (1<<opposite_teams_pieces[3]))):
                    if ((board_copy[2]) & (1<<opposite_teams_pieces[3])):
                        board_copy[2] ^= 1<<opposite_teams_pieces[3]
                        points += 1
                    elif ((board_copy[3]) & (1<<opposite_teams_pieces[3])):
                        board_copy[3] ^= 1<<opposite_teams_pieces[3]
                        points += 1
                else:
                    print("Red King invalid move")
                    return False, 0
            elif player == 'B':
                if ((move_to_index == piece_index + 9) and ((board_copy[0] | board_copy[1]) & (1<<opposite_teams_pieces[0]))):
                    if ((board_copy[0]) & (1<<opposite_teams_pieces[0])):
                        board_copy[0] ^= 1<<opposite_teams_pieces[0]
                        points += 1
                    elif ((board_copy[1]) & (1<<opposite_teams_pieces[0])):
                        board_copy[1] ^= 1<<opposite_teams_pieces[0]
                        points += 1
                elif ((move_to_index == piece_index + 7) and ((board_copy[0] | board_copy[1]) & (1<<opposite_teams_pieces[1]))):
                    if ((board_copy[0]) & (1<<opposite_teams_pieces[1])):
                        board_copy[0] ^= 1<<opposite_teams_pieces[1]
                        points += 1
                    elif ((board_copy[1]) & (1<<opposite_teams_pieces[1])):
                        board_copy[1] ^= 1<<opposite_teams_pieces[1]
                        points += 1
                elif ((move_to_index == piece_index - 7) and ((board_copy[0] | board_copy[1]) & (1<<opposite_teams_pieces[2]))):
                    if ((board_copy[0]) & (1<<opposite_teams_pieces[2])):
                        board_copy[0] ^= 1<<opposite_teams_pieces[2]
                        points += 1
                    elif ((board_copy[1]) & (1<<opposite_teams_pieces[2])):
                        board_copy[1] ^= 1<<opposite_teams_pieces[2]
                        points += 1
                elif ((move_to_index == piece_index - 9) and ((board_copy[0] | board_copy[1]) & (1<<opposite_teams_pieces[3]))):
                    if ((board_copy[0]) & (1<<opposite_teams_pieces[3])):
                        board_copy[0] ^= 1<<opposite_teams_pieces[3]
                        points += 1
                    elif ((board_copy[1]) & (1<<opposite_teams_pieces[3])):
                        board_copy[1] ^= 1<<opposite_teams_pieces[3]
                        points += 1
                else:
                    print("Black King invalid move")
                    return False, 0
    elif not is_king:
        r_jumps = [piece_index - 7, piece_index - 9]
        b_jumps = [piece_index + 7, piece_index + 9]
        if player == 'R':
            even_moves = [piece_index - 4, piece_index - 5]
            odd_moves = [piece_index - 3, piece_index - 4]
            if piece_index in even_rows and move_to_index in even_moves:
                pass
            elif piece_index in odd_rows and move_to_index in odd_moves:
                pass
            elif move_to_index in r_jumps:
                if ((move_to_index == piece_index - 9) and (piece_index in even_rows) and ((board_copy[2] | board_copy[3]) & (1<<piece_index-5))):
                    if ((board_copy[2]) & (1<<piece_index-5)):
                        board_copy[2] ^= 1<<piece_index-5
                        points += 1
                    elif ((board_copy[3]) & (1<<piece_index-5)):
                        board_copy[3] ^= 1<<piece_index-5
                        points += 1
                elif ((move_to_index == piece_index - 9) and (piece_index in odd_rows) and ((board_copy[2] | board_copy[3]) & (1<<piece_index-4))):
                    if ((board_copy[2]) & (1<<piece_index-4)):
                        board_copy[2] ^= 1<<piece_index-4
                        points += 1
                    elif ((board_copy[3]) & (1<<piece_index-4)):
                        board_copy[3] ^= 1<<piece_index-4
                        points += 1
                elif ((move_to_index == piece_index - 7) and (piece_index in even_rows) and ((board_copy[2] | board_copy[3]) & (1<<piece_index-4))):
                    if ((board_copy[2]) & (1<<piece_index-4)):
                        board_copy[2] ^= 1<<piece_index-4
                        points += 1
                    elif ((board_copy[3]) & (1<<piece_index-4)):
                        board_copy[3] ^= 1<<piece_index-4
                        points += 1
                elif ((move_to_index == piece_index - 7) and (piece_index in odd_rows) and ((board_copy[2] | board_copy[3]) & (1<<piece_index-3))):
                    if ((board_copy[2]) & (1<<piece_index-3)):
                        board_copy[2] ^= 1<<piece_index-3
                        points += 1
                    elif ((board_copy[3]) & (1<<piece_index-3)):
                        board_copy[3] ^= 1<<piece_index-3
                        points += 1
                else:
                    print("Red Piece board[2] or [3]")
                    return False, 0
            else:
                return False, 0
        elif player == 'B':
            even_moves = [piece_index + 3, piece_index + 4]
            odd_moves = [piece_index + 4, piece_index + 5]
            if piece_index in even_rows and move_to_index in even_moves:
                pass
            elif piece_index in odd_rows and move_to_index in odd_moves:
                pass
            elif move_to_index in b_jumps:
                if ((move_to_index == piece_index + 9) and (piece_index in even_rows) and ((board_copy[0] | board_copy[1]) & (1<<piece_index+4))):
                    if ((board_copy[0]) & (1<<piece_index+4)):
                        board_copy[0] ^= 1<<piece_index+4
                        points += 1
                    elif ((board_copy[1]) & (1<<piece_index+4)):
                        board_copy[1] ^= 1<<piece_index+4
                        points += 1
                elif ((move_to_index == piece_index + 9) and (piece_index in odd_rows) and ((board_copy[0] | board_copy[1]) & (1<<piece_index+5))):
                    if ((board_copy[0]) & (1<<piece_index+5)):
                        board_copy[0] ^= 1<<piece_index+5
                        points += 1
                    elif ((board_copy[1]) & (1<<piece_index+5)):
                        board_copy[1] ^= 1<<piece_index+5
                        points += 1
                elif ((move_to_index == piece_index + 7) and (piece_index in even_rows) and ((board_copy[0] | board_copy[1]) & (1<<piece_index+3))):
                    if ((board_copy[0]) & (1<<piece_index+3)):
                        board_copy[0] ^= 1<<piece_index+3
                        points += 1
                    elif ((board_copy[1]) & (1<<piece_index+3)):
                        board_copy[1] ^= 1<<piece_index+3
                        points += 1
                elif ((move_to_index == piece_index + 7) and (piece_index in odd_rows) and ((board_copy[0] | board_copy[1]) & (1<<piece_index+4))):
                    if ((board_copy[0]) & (1<<piece_index+4)):
                        board_copy[0] ^= 1<<piece_index+4
                        points += 1
                    elif ((board_copy[1]) & (1<<piece_index+4)):
                        board_copy[1] ^= 1<<piece_index+4
                        points += 1
                else:
                    return False, 0
            else:
                return False, 0

    if (board_copy[0] & (1<<piece_index)):
        board_copy[0] ^= 1 << piece_index
        board_copy[0] ^= 1 << move_to_index
        
    if (board_copy[1] & (1<<piece_index)):
        board_copy[1] ^= 1 << piece_index
        board_copy[1] ^= 1 << move_to_index  # this block swaps the bits (or checkers pieces) after all conditions have been passed
        
    if (board_copy[2] & (1<<piece_index)):
        board_copy[2] ^= 1 << piece_index
        board_copy[2] ^= 1 << move_to_index
        
    if (board_copy[3] & (1<<piece_index)):
        board_copy[3] ^= 1 << piece_index
        board_copy[3] ^= 1 << move_to_index

    # king me below
    for i in range(4):
        if (board_copy[0] & (1<<i)):
            board_copy[0] ^= 1 << i
            board_copy[1] ^= 1 << i
    for i in range(28, 32):
        if (board_copy[2] & (1<<i)):
            board_copy[2] ^= 1 << i
            board_copy[3] ^= 1 << i

    return board_copy, points

initialize_game()
bb.print_board(board)
player = 'R'
round_num = 1
game_on = True
while game_on:
    before_move = board.copy()
    new_board = board.copy()
    print("Team {}'s move".format(player))
    piece_index = int(input("select a piece to move: "))
    input_move_to = int(input("select a location to move to: "))
    new_board, points = make_move(piece_index, input_move_to, new_board, player)
    if not new_board:
        print("Not a valid move, try again!")
    else:
        board = new_board
        training_data_into_DB(board, before_move, player, round_num, points)
        player = 'R' if player == 'B' else 'B'
        round_num += 1 if player == 'R' else 0 # we only want to increment the round num after both teams have gone

    bb.print_board(board)
    game_on = True if ((board[0] or board[1]) and (board[2] or board[3])) else False # if one side or the other is 0, game over

if not game_on:
    winner = 'R' if (board[0] or board[1]) else 'B' # game is over, insert winning into db
    game_results_into_DB(winner)
        







