from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

s = Solution()

case1_nums = [1,1,2]
print(s.removeDuplicates(case1_nums)) # 2, nums = [1,2,_]

case2_nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(case2_nums)) # 5, nums = [0,1,2,3,4,_,_,_,_,_]