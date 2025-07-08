from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and target - (nums[i] + nums[j]) == 0:
                    return [i, j]
                
class OptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

s = OptimizedSolution()
case1_nums = [2,7,11,15]
case1_target = 9
print(s.twoSum(case1_nums, case1_target)) # [0, 1]

case2_nums = [3,2,4]
case2_target = 6
print(s.twoSum(case2_nums, case2_target)) # [1, 2]

case3_nums = [3,3]
case3_target = 6
print(s.twoSum(case3_nums, case3_target)) # [0, 1]

case4_nums = [0,4,3,0]
case4_target = 0
print(s.twoSum(case4_nums, case4_target)) # [0, 3]

case5_nums = [-3,4,3,90]
case5_target = 0
print(s.twoSum(case5_nums, case5_target)) # [0, 2]

case6_nums = [-1,-2,-3,-4,-5]
case6_target = -8
print(s.twoSum(case6_nums, case6_target)) # [2, 4]


