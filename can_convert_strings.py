"""
Given two strings s and t, your goal is to convert s into t in k moves or less.

During the ith (1 <= i <= k) move you can:

Choose any index j (1-indexed) from s, such that 1 <= j <= s.length 
and j has not been chosen in any previous move, and shift the character at that index i times.
Do nothing.
Shifting a character means replacing it by the next letter in the 
alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character by i 
means applying the shift operations i times.

Remember that any index j can be picked at most once.

Return true if it's possible to convert s into t in no more than k moves, otherwise return false.
 
"""

#the only difficulty is handling the wrap around 
def canConvertStrings(s,t,k):
    #if the strings arent equal length. 
    shift_counter = 0
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        print(shift_counter)
        # if(shift_counter > k):
        #     return False
        if s[i] != t[i]:
            ch1 = ord(s[i])
            ch2 = ord(t[i])
            if(ch2 > ch1):
                shift_counter += (ch2 - ch1)
            else:
                shift_counter +=(122 - ch1 + ch2 -97)
    return True

s = "input"
t = "ouput"
k = 9
print(canConvertStrings(s, t, k))
        
            
    