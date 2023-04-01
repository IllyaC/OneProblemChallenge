"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range 
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
def reverse(integer):
    int_min = -2 ** 31
    int_max = 2 **31 -1
    isNegative = False
    
    if integer < 0:
        isNegative = True
        integer = -integer
    reversed_integer = 0
    
    while integer != 0:
        digit = integer%10
        integer //= 10
        
        if reversed_integer > (int_max -digit) // 10:
            return 0
        reversed = reversed_integer * 10 + digit
    if(isNegative):
        reversed_integer = -reversed_integer
    return reversed_integer
integer  = 1563847412
print(reverse(integer))
2147483651
2147483647