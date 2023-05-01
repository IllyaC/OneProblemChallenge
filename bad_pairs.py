"""
You are given a 0-indexed integer array nums. \
A pair of indices (i, j) is a bad pair if i < j 
and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
"""
#j - nums[j] = i - nums[i] is a good pair 
# total number of pairs is len(nums)C2
def countBadPairs(nums):
    sums = {}
    bad_pairs = 0
    for i in range(len(nums)):
        if i - nums[i]  in sums:
            sums[i-nums[i]] +=1
        else:
            sums[i-nums[i]]  = 1
        bad_pairs += (i - sums[i-nums[i]]) +1 
        print(sums, sums[i-nums[i]], i, bad_pairs)
    return bad_pairs


nums = [4, 1, 3, 3]
print(countBadPairs(nums))