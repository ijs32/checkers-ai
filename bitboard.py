from MySQLConn import conn

BITMASK = 0b11111111111111111111111111111111
board = [
    0b00000000000000000000000000000000, # red king 32 bit board
    0b11111111111100000000000000000000, # red piece 32 bit board
    0b00000000000000000000000000000000, # black king 32 bit board
    0b00000000000000000000111111111100  # black piece 32 bit board
] 

def make_move(piece_index, move_to_index):
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
    def boardDB():
    def king_me(board):
        for i in range(4):
            if (board[1] & (1<<i)):
                board[1] ^= 1 << i
                board[0] ^= 1 << i
        for i in range(28, 32):
            if (board[3] & (1<<i)):
                board[3] ^= 1 << i
                board[2] ^= 1 << i
        
    if ((((board[0] | board[1] | board[2] | board[3]) ^ BITMASK) & (1<<move_to_index))):
        if (board[0] & (1<<piece_index)):
            board[0] ^= 1 << piece_index
            board[0] ^= 1 << move_to_index
        if (board[1] & (1<<piece_index)):
            board[1] ^= 1 << piece_index
            board[1] ^= 1 << move_to_index
        if (board[2] & (1<<piece_index)):
            board[2] ^= 1 << piece_index
            board[2] ^= 1 << move_to_index
        if (board[3] & (1<<piece_index)):
            board[3] ^= 1 << piece_index
            board[3] ^= 1 << move_to_index

        king_me(board)
        return board
    else:
        return 0

def print_board():
    positions = {}
    for i in range(32):
        if (board[0] & (1<<i)):
            positions["piece{0}".format(i)] = "RK"
        elif(board[1] & (1<<i)):
            positions["piece{0}".format(i)] = "RP"
        elif(board[2] & (1<<i)):
            positions["piece{0}".format(i)] = "BK"
        elif(board[3] & (1<<i)):
            positions["piece{0}".format(i)] = "BP"
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


print_board()
game_on = True
while game_on:
    piece_index = int(input("select a piece to move: "))
    input_move_to = int(input("select a location to move to: "))
    new_board = make_move(piece_index, input_move_to)
    print("this is new_board: ", new_board)
    if not new_board:
        print("Not a valid move!")
    else:
        board = new_board
    print_board()
    game_on = True if ((board[0] | board[1]) or (board[2] | board[3])) else False
        






# non destroyed version of board
'''
    -------------------------------------------------------------------------
    |        |31******|        |30******|        |29******|        |28******|
    |        |***31***|        |***30***|        |***29***|        |***28***|
    |        |********|        |********|        |********|        |========|
    |________|________|________|________|________|________|________|________|
    |27******|        |26******|        |25******|        |24******|        |
    |***27***|        |***26***|        |***25***|        |***24***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |23******|        |22******|        |21******|        |20******|
    |        |***23***|        |***22***|        |***21***|        |***20***|
    |        |========|        |========|        |========|        |========|
    |________|________|________|________|________|________|________|________|
    |19******|        |18******|        |17******|        |16******|        |
    |***19***|        |***18***|        |***17***|        |***16***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |15******|        |14******|        |13******|        |12******|
    |        |***15***|        |***14***|        |***13***|        |***12***|
    |        |========|        |========|        |========|        |========|
    |________|________|________|________|________|________|________|________|
    |11******|        |10******|        |09******|        |08******|        |
    |***11***|        |***10***|        |***09***|        |***08***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
    |        |07******|        |06******|        |05******|        |04******|
    |        |***07***|        |***06***|        |***05***|        |***04***| 
    |        |========|        |========|        |========|        |========|
    |________|________|________|________|________|________|________|________|
    |03******|        |02******|        |01******|        |00******|        |
    |***03***|        |***02***|        |***01***|        |***00***|        |
    |********|        |********|        |********|        |********|        |
    |________|________|________|________|________|________|________|________|
'''

'''

BP = 0b11111111101111111111111111111111
BK = 0b11111111101111111111111111111111
RP = 0b11111111101111111111111111111111
RK = 0b11111111101111111111111111111111

print("this is RP: ", (bin(RP)[2:].zfill(32)))
print("this is length: ", (len(bin(RP)[2:].zfill(32))))
for i in range(len(bin(RP)[2:].zfill(32))):
    if ((((RP | RK | BP | BK) ^ BITMASK) & (1<<i))):
        print("this is the 0: ", i)
    else:
        print("this is the 1: ", i)
board = []
print(len(bin(RP)[2:]))
for i in range(len(bin(RP)[2:])):
    board.append(0)
    if (RP & (1<<i)):
        board.append("RP")
    if(BP & (1<<i)):
        board.append("BP")
    if(RK & (1<<i)):
        board.append("RK")
    if(BK & (1<<i)):
        board.append("BK")
print("this is board: ", board)
print("combined board: ", bin(BP ^ BK ^ RP ^ RK))
# print(bin(BP)[2:].zfill(32))
# BP ^= 1 << 31
# print(bin(BP)[2:].zfill(32))
print(bin(RP)[2:].zfill(32)) 
if (RP | (1<<19)):
    RP ^= 1 << 19
    RP ^= 1 << 23

print(bin(RP)[2:].zfill(32)) 
0b11111111011100100000000000000000        

0b0101010110101010000101010010000000000000000000000000000000000000

0b1111 0b11111111011110000000000000000000
  1111
  1111
  0000   
  0000   
  0000   
  0000   
  0000   
'''