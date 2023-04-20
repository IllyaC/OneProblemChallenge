"""
You are given two integer arrays nums1 and nums2 both of the same length. 
The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.


"""
def advantageCount(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    final_arr = [0] * len(nums1)
    nums1.sort()
    indexed_arr2 = list(enumerate(nums2))
    sorted_indexed_arr2 = sorted(indexed_arr2, key=lambda i: i[1])
    sorted_arr2_with_indexes = [(i[1], i[0]) for i in sorted_indexed_arr2]
    pointer_1, pointer_2, pointer_3 = 0, len(nums1)-1, len(nums1)-1
    
    while pointer_1 != pointer_2:
        if nums1[pointer_2] > sorted_arr2_with_indexes[pointer_3][1]:
            final_arr[sorted_arr2_with_indexes[pointer_3][1]] = nums1[pointer_2]
            pointer_2-=1
            pointer_3 -=1
        else:
            final_arr[sorted_arr2_with_indexes[pointer_3][1]] = nums1[pointer_1]
            pointer_1 +=1
            pointer_3-=1
    
    final_arr[sorted_arr2_with_indexes[pointer_3][1]] = nums1[pointer_1]
    return final_arr  
    


nums1 = [12,24,8,32]
nums2 = [13,25,32,11]
print(advantageCount(nums1,nums2))


        
    
    
    