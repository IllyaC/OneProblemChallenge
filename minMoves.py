"""
You are given an integer array nums of even 
length n and an integer limit. In one move, 
you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices 
i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. 
For example, the array [1,2,3,4] is complementary because for all indices 
i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.
"""
def minMoves(nums, limit):
    fist_half = 0
    second_half = len(nums)
    if(len(nums) == 2):
        return 0
    
    sum_pairs = {}
    for i in range(len(nums)//2):
        sum = nums[i] + nums[len(nums)-1-i]
        if sum in sum_pairs:
            sum_pairs[sum] += 1
        else:
            sum_pairs[sum] = 1
    
    selected_sum = max(sum_pairs, key=lambda item: sum_pairs[item])
    
    if(sum_pairs[selected_sum] == 1):
        total_sum = 0
        for key in sum_pairs:
            total_sum += key
        num_elements = len(sum_pairs)
        average = total_sum/num_elements
        least_distance = 10000
        for key in sum_pairs:
            distance = abs(key -average)
            if(distance < least_distance):
                selected_sum = key
            
    moves_counter = 0 
    for i in range(len(nums)//2):
        sum = nums[i] + nums[len(nums)-1-i]
        left = nums[i]
        right = nums[len(nums)-1-i]
        if(sum != selected_sum):
            if(sum < selected_sum):
                if(left + limit or right + limit) >= selected_sum:
                    moves_counter +=1
                    continue
                else:
                    moves_counter +=2
                    continue
            if(sum > selected_sum):
                if(left + 1 or right + 1) <= selected_sum:
                    moves_counter +=1
                    continue
                else:
                    moves_counter +=2
                    continue               
    return moves_counter

nums = [1, 2, 4, 3]
print(minMoves(nums, 2))