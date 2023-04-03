def rob(nums):
        total_money = 0 
        max_index = len(nums)-1
        if len(nums) == 0 :
            return 0
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)//2):
            current_steal = max(nums)
            house_index = nums.index(current_steal)
            print(house_index)
            
            if(house_index == max_index):
                if nums[max_index-1] == -1:
                    continue
                total_money += current_steal
                nums[house_index] = -1
                nums[0] = 0
                nums[house_index-1] = 0
                continue
            if(house_index == [0] and nums[max_index] == -1):
                continue
            if(nums[house_index+1] ==-1 or nums[house_index-1] == -1):
                continue
            
            nums[house_index] = -1
            nums[house_index-1] = 0
            nums[house_index+1] = 0
            total_money += current_steal
        return total_money

houses = [1, 7, 9, 4, 6]
print(rob(houses))
        