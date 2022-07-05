import os
import numpy as np

BP = 0b00000000000000000000111111111111
BK = 0b00000000000000000000000000000000
RP = 0b11111111111100000000000000000000
RK = 0b00000000000000000000000000000000

def make_move(piece_type, piece_index, move):
    if (move == "FR"):
        move_to_index = piece_index +
    if (BK | (1<<move_to_index) and BP | (1<<move_to_index) and RP | (1<<move_to_index) and RK | (1<<move_to_index)):
        piece_type ^= 1 << piece_index
        piece_type ^= 1 << move_to_index
        return piece_type

print("before function: ", bin(RP)[2:])
print("after function:  ", bin(make_move(RP, 19, 23))[2:])

'''
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
# 0b01010101  0b1111  0b11111111011110000000000000000000
#   10101010    1111 
#   00010101    0111 
#   10000000    1000 
#   00000000    0000
#   10101010    0000
#   01010101    0000
#   10101010    0000
'''