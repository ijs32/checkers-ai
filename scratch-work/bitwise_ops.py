n1 = 0b000000000001
n2 = 0b000000000000
n3 = 0b00000000000
n4 = 0b00000000000

board = [
    0b00000000000000000000000000000000, # red king 32 bit board
    0b11111111111100000000000000000000, # red piece 32 bit board
    0b00000000000000000000000000000000, # black king 32 bit board
    0b00000000000000000000111111111111  # black piece 32 bit board
] 

new_board = board.copy()

for i in range(28, 32):
    print(i)
if n1 & (1<< 0):
    n1 ^= 1 << 0
    n2 ^= 1 << 0

print(bin(n1)[2:].zfill(12))
print(bin(n2)[2:].zfill(12))
# print(bin(n1)[2:])
# print(bin(n2)[2:])

# AND
# both bits must be 1
# 0  1  0  1
# 0  0  1  1
# =  =  =  =
# 0  0  0  1

# n3 = n1 & n2

# print("AND operator")
# print("number {} is {} in binary".format(n3, bin(n3)[2:]))

# OR
# unless all bits are 0 the bit is 1
# 0  1  0  1
# 0  0  1  1
# =  =  =  =
# 0  1  1  1


game_on = True if ((n1 | n2) or (n3 | n4)) else False
print(game_on)
# print("OR operator")
# print("number {} is {} in binary".format(n3, bin(n3)[2:]))

# XOR
# If the values are different = 1 else = 0
# 0 1 1 0
# 0 0 1 1
# = = = =
# 0 1 0 1

# n3 = n1 ^ n2

# print("XOR operator")
# print("number {} is {} in binary".format(n3, bin(n3)[2:]))

# NOT
# bit_inverter = 0b111111111111111
# print("original binary: ", bin(n1)[2:])
# print("inverted binary: ", ("0" + bin(bit_inverter - n1)[2:]))

# SHIFTS
# left shifting a number is akin to multiplying it by two, when you shift all numbers to the left you double them
# right shifting on the other hand divides a number by two for the same reason
# the number after the >>= or <<= stands for how many places you want to shift it
# n1 = 20

# print(bin(n1)[2:])
# n1 <<= 1
# print(bin(n1)[2:])
# by right shifting the number we return it to 20
# print(bin(n1)[2:])
# n1 >>= 2
# print(bin(n1)[2:])

# 
# FLAGS
# 

# Read, Write, Execute, Change Policy

person1 = 0b1100
person2 = 0b1110
person3 = 0b1111
person4 = 0b1101
person5 = 0b1110

together1 = person1 & person2 & person3 & person4 & person5
together2 = person1 | person2 | person3 | person4 | person5
print(bin(together2)[2:])

READ = 0b1000
WRITE = 0b0100
EXECUTE = 0b0010
CHANGE_POLICY = 0b0001

def myFunction(permission):
    print(bin(permission)[2:])

# myFunction(READ | WRITE)

# a = 10 #01010
# b = 20 #10100

# a ^= b #11110
# b ^= a #01010
# a ^= b #10100

# print(a)
# print(b)

#using bitwise to check even or odd

random_number = 89234759241
if random_number & 1 == 0:
    print("even")
else:
    print("odd")

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