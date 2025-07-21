from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                if index == -1:
                    index = i
        if index == -1 : return len(nums)
        return index
    
s = Solution()
case1_nums = [1,3,5,6]
case1_target = 5
print(s.searchInsert(case1_nums, case1_target)) # 2

case2_nums = [1,3,5,6]
case2_target = 2
print(s.searchInsert(case2_nums, case2_target)) # 1

case3_nums = [1,3,5,6]
case3_target = 7
print(s.searchInsert(case3_nums, case3_target)) # 4