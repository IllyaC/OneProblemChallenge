"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can 
remove either the leftmost stone or the rightmost stone from the row and 
receive points equal to the sum of the remaining stones' values in the row. 
The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so 
he decided to minimize the score's difference. Alice's goal is to maximize the 
difference in the score.

Given an array of integers stones where stones[i] represents the value of the 
ith stone from the left, return the difference in Alice and Bob's score if they 
both play optimally.
"""
"""
Alice always wins because obviously she as one more number to work with compared to bob. if there is 5 numbers
Alice will get the sum of 4 and 2 meanwhile Bob will get the sum of 3 and 1 
if there are 6 a gets 5 then 3 then 1 while bob gets 4 then 2 
"""
def stoneGameVII(stones):
    n = len(stones)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if length % 2 == 1:  # Alice's turn
                if left == 0:
                    dp[left][right] = stones[right] - dp[left][right - 1]
                elif right == n - 1:
                    dp[left][right] = stones[left] - dp[left + 1][right]
                else:
                    dp[left][right] = max(stones[left] - dp[left + 1][right],
                                          stones[right] - dp[left][right - 1])
            else:  # Bob's turn
                if left == 0:
                    dp[left][right] = -stones[right] - dp[left][right - 1]
                elif right == n - 1:
                    dp[left][right] = -stones[left] - dp[left + 1][right]
                else:
                    dp[left][right] = min(-stones[left] - dp[left + 1][right],
                                          -stones[right] - dp[left][right - 1])

    return dp[0][n - 1]


stones = [7,90,5,1,100,10,10,2]
print(stoneGameVII(stones))            
            