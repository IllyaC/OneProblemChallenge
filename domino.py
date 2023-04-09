"""
Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on 
the board such that exactly one of the tilings has both squares occupied by a tile.
"""

def numTiling(n):
    total = 0 
    if n == 1:
        return 1
    dp1 = 5
    dp2 = 2 
    cumsum = 4
    for i in range(3, n):
        total = dp1 + dp2 +cumsum 
        cumsum+=dp2*2
        dp2 = dp1
        dp1 = total 
        print(total, cumsum, dp2, dp1)
        
    return total%10**9+7
    
    
number = 6
 


print(numTiling(number))