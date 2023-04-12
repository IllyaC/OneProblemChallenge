from math import comb
"""
Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. 
Since the answer may be too large, return it modulo 109 + 7.
"""

def numWays(s):
    ones_counter = 0
    ones_positions = []
    final_comb = 0
    first_position, second_position, third_position = 0, 0, 0
    
    for i in range(len(s)):
        if s[i] == "1":
            ones_counter +=1
            ones_positions.append(i)
    
    if(ones_counter == 0):
        return comb(len(s)-1, 2)
    if(ones_counter < 3 or ones_counter % 3 !=0):
        return 0
    print(ones_positions)
    first_position = ones_positions[(ones_counter // 3 - 1)]
    second_position = ones_positions[ones_counter//3]
    second_position_far = ones_positions[(ones_counter//3)*2-1]
    third_position  = ones_positions[ones_counter//3 *2]
    print(first_position, second_position, third_position, second_position_far)
    final_comb = (second_position - first_position) * (third_position - second_position_far)
    print(final_comb)
    return final_comb    
    
        
    

        
s = "100100010100110"
print(numWays(s))
# 1 1 0001
# 1 10 001
# 1 100 01
# 1 1000 1

# 1 0001
# 10 0001
# 100 01
# 1000 1

# 10 1
# 1 01

# 1 001
# 10 01
# 100  1
