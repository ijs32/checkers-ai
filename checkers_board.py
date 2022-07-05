import os
import numpy as np

BP = 0b00000000000000000000111111111111
BK = 0b00000000000000000000000000000000
RP = 0b11111111111100000000000000000000
RK = 0b00000000000000000000000000000000

def make_move(piece_board, piece_type, piece_index, move):
    
    if (move == "FR"):
        move_to_index = piece_index - 4
    elif(move == "FL"):
        move_to_index = piece_index - 6
    elif(move == "BR" and piece_type == "BK" or piece_type == "RK"):
        move_to_index = piece_index + 4
    elif(move == "FL" and piece_type == "BK" or piece_type == "RK"):
        move_to_index = piece_index + 6

    if (BK | (1<<move_to_index) and BP | (1<<move_to_index) and RP | (1<<move_to_index) and RK | (1<<move_to_index)):
        piece_board ^= 1 << piece_index
        piece_board ^= 1 << move_to_index
        return piece_board

RK = 0b11111111011110000000000000000000
print("before function: ", bin(RK)[2:])
print("after function:  ", bin(make_move(RK, "RK", 19, "BR"))[2:])

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