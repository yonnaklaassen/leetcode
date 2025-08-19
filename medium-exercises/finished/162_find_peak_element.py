from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = nums[0]
        index_peak = 0
        for index, num in enumerate(nums, start=0):
            if num > peak:
                peak = num
                index_peak = index
        return index_peak
    
s = Solution()
case1_nums = [1, 2, 3, 1]
print(s.findPeakElement(case1_nums)) # 2

case2_nums = [1,2,1,3,5,6,4]
print(s.findPeakElement(case2_nums)) # 5