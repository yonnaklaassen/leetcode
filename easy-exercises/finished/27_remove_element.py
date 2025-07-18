from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
s = Solution()

case1_nums = [3,2,2,3]
case1_val = 3
print(s.removeElement(case1_nums, case1_val)) # k = 3, nums = = [2,2,_,_]

case2_nums = [0,1,2,2,3,0,4,2]
case2_val = 2
print(s.removeElement(case2_nums, case2_val)) # k = 5, nums = [0,1,4,0,3,_,_,_]