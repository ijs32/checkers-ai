import os
import numpy as np


BITMASK = 0b11111111111111111111111111111111
r_k = 0b00000000010000000000000000000000 # red king 32 bit board
r_p = 0b11111111001101000000000000000000 # red piece 32 bit board
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