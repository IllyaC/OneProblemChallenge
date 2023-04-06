"""
Given an integer array nums, return an array 
answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is 
guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in 
O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
        forwards_then_backwards = 1
        multiplications = [1] * len(nums)
        for i in  range(len(nums)):
            multiplications[i] = forwards_then_backwards
            forwards_then_backwards *= nums[i]
        forwards_then_backwards = 1
        for j in  range(len(nums)-1, -1, -1):
            multiplications[j] *= forwards_then_backwards
            forwards_then_backwards *= nums[j]

        return multiplications

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
     
        
        
        