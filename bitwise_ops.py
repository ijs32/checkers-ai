import os
import numpy as np

n1 = 23477
n2 = 31213

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

# n3 = n1 | n2

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
# print(bin(together2)[2:])

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