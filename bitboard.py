import os
import numpy as np


BITMASK = 0b11111111111111111111111111111111
r_k = 0b00000000000000000000000000000000 # red king 32 bit board
r_p = 0b11111111111100000000000000000000 # red piece 32 bit board
b_k = 0b00000000000000000000000000000000 # black king 32 bit board
b_p = 0b00000000000000000000111111111111 # black piece 32 bit board

def make_move(piece_board, piece_type, piece_index, move):
    # movement will of course be different as it is relative to starting position
    # next I am going to limit piece movement for border pieces by hard coding some border arrays and checking if piece_index in border_array:
    if(piece_type == "RP" or piece_type == "RK"):
        if (move == "FR"):
            move_to_index = piece_index - 4
        elif(move == "FL"):
            move_to_index = piece_index - 6
        elif(move == "BR" and piece_type == "RK"):
            move_to_index = piece_index + 4
        elif(move == "FL" and piece_type == "RK"):
            move_to_index = piece_index + 6
    elif(piece_type == "BP" or piece_type == "BK"):
        if (move == "FR"):
            move_to_index = piece_index + 4
        elif(move == "FL"):
            move_to_index = piece_index + 6
        elif(move == "BR" and piece_type == "BK"):
            move_to_index = piece_index - 4
        elif(move == "FL" and piece_type == "BK"):
            move_to_index = piece_index - 6

    if ((((b_k | b_p | r_p | r_k) ^ BITMASK) & (1<<move_to_index))):
        piece_board ^= 1 << piece_index
        piece_board ^= 1 << move_to_index
        return piece_board
    else:
        return piece_board

# RK = 0b11111111011110000000000000000000
# print("before function:   ", bin(r_k)[2:].zfill(32))
# print("after function:    ", bin(make_move(r_k, "RK", 22, "FR"))[2:].zfill(32))
# print("After function RP: ", bin(r_p)[2:].zfill(32))
# print("After function BK: ", bin(b_k)[2:].zfill(32))
# print("After function BP: ", bin(b_p)[2:].zfill(32))

# testing stuff
positions = {}
for i in range(len(bin(r_p)[2:])):
    if (r_p & (1<<i)):
        positions["piece{0}".format(i)] = "RP"
    elif(b_p & (1<<i)):
        positions["piece{0}".format(i)] = "BP"
    elif(r_k & (1<<i)):
        positions["piece{0}".format(i)] = "RK"
    elif(b_k & (1<<i)):
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
print(positions)
print("this is length: ", (len(bin(r_p)[2:].zfill(32))))
print(f'''
-------------------------------------------------------------------------
|        |32******|        |31******|        |30******|        |29******|
|        |***{p31}***|        |***{p30}***|        |***{p29}***|        |***{p28}***|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|
|28******|        |27******|        |26******|        |25******|        |
|***{p27}***|        |***{p26}***|        |***{p25}***|        |***{p24}***|
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|
|        |24******|        |23******|        |22******|        |21******|
|        |***{p23}***|        |***{p22}***|        |***{p21}***|        |***{p20}***|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|20******|        |19******|        |18******|        |17******|        |
|***{p19}***|        |***{p18}***|        |***{p17}***|        |***{p16}***|
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|        
|        |16******|        |15******|        |14******|        |13******|
|        |***{p15}***|        |***{p14}***|        |***{p13}***|        |***{p12}***|  
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|12******|        |11******|        |10******|        |09******|        |
|***{p11}***|        |***{p10}***|        |***{p09}***|        |***{p08}***|
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|        
|        |08******|        |07******|        |06******|        |05******|
|        |***{p07}***|        |***{p06}***|        |***{p05}***|        |***{p04}***| 
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|04******|        |03******|        |02******|        |01******|        |
|***{p03}***|        |***{p02}***|        |***{p01}***|        |***{p00}***|        |
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|        
''')
# non destroyed version of board
'''
-------------------------------------------------------------------------
|        |32******|        |31******|        |30******|        |29******|
|        |***{}***|        |***{}***|        |***{}***|        |***{}***|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|
|28******|        |27******|        |26******|        |25******|        |
|***{}***|        |***{}***|        |***{}***|        |***{}***|        |
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|
|        |24******|        |23******|        |22******|        |21******|
|        |***{}***|        |***{}***|        |***{}***|        |***{}***|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|20******|        |19******|        |18******|        |17******|        |
|********|        |********|        |********|        |********|        |
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|        
|        |16******|        |15******|        |14******|        |13******|
|        |********|        |********|        |********|        |********|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|12******|        |11******|        |10******|        |09******|        |
|***RP***|        |***RP***|        |***RP***|        |***RP***|        |
|********|        |********|        |********|        |********|        |
|________|________|________|________|________|________|________|________|        
|        |08******|        |07******|        |06******|        |05******|
|        |***RP***|        |***RP***|        |***RP***|        |***RP***|
|        |********|        |********|        |********|        |********|
|________|________|________|________|________|________|________|________|                 
|04******|        |03******|        |02******|        |01******|        |
|***RP***|        |***RP***|        |***RP***|        |***RP***|        |
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