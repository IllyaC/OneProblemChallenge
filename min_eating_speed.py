import math
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile 
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she 
eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

def minEatingSpeed(piles, h):
    start, end = 1, 10 **9
    while start <= end:
        eating_rate = ((start+end))//2
        total = 0 
        for pile in piles:
            pile_divided = pile//eating_rate
            total += int(math.ceil(pile_divided))
        if total > h:
            start = eating_rate +1
        else:
            end = eating_rate -1
    return total
            
piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))

        
        