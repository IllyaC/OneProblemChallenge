"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range 
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
def reverse(integer):
    reversed_integer = 0
    isNegative = integer < 0
    original_integer = abs(integer)
    integer  = abs(integer)
    digit_counter = -1
    
    if(integer == -2147483648):
        return reversed_integer
    
    
        
    while(integer != 0):
        digit_counter +=1 
        integer = integer // 10
    
    
    integer = original_integer
    hitMax = digit_counter == 9
    prevHitMax = False

  
    for digit in range(digit_counter+1):
        
        temp = integer%10
        if hitMax:
            if digit_counter == 9:
                        if temp == 2:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 2:
                            return 0
            if digit_counter == 8  and prevHitMax:
                        if temp ==1:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp >1:
                            return 0
            if digit_counter == 7 and temp >4 and prevHitMax:
                        if temp == 4:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        return 0
            if digit_counter == 6 and prevHitMax:
                        if temp == 7:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 7:
                            return 0
            if digit_counter == 5  and prevHitMax:
                        if temp == 4:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp>4:
                            return 0
            if digit_counter == 4 and prevHitMax:
                        if temp == 8:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 8:
                            return 0
            if digit_counter == 3  and prevHitMax:
                        if temp == 3:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 3:
                            return 0
            if digit_counter == 2  and prevHitMax:
                        if temp == 6:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 6:
                            return 0
            if digit_counter == 1 and prevHitMax:
                        if temp == 4:
                            prevHitMax = True
                        else: 
                            prevHitMax = False
                        if temp > 4:
                            return 0
            if digit_counter == 0 and temp >7 and prevHitMax:
                        return 0
        
            
        reversed_integer += temp * (10 **digit_counter)
        digit_counter -= 1
        integer = integer // 10
    
    if(isNegative):
        reversed_integer = reversed_integer * -1
    
   
    return reversed_integer
    
        
        
integer  = 1563847412
print(reverse(integer))
2147483651
2147483647