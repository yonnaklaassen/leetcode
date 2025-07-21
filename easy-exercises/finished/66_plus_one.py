from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        n = len(digits)
        for digit in digits:
            sum = digit * (10**(n - 1))
            total += sum
            n = n - 1 
        append = []
        string_num = str(total + 1)
        for i in range(len(string_num)):
            append.append(int(string_num[i]))
        return append
    
s = Solution()
case1 = [1,2,3]
print(s.plusOne(case1)) # [1,2,4]

case2 = [4,3,2,1]
print(s.plusOne(case2)) # [4,3,2,2]

case3 = [9]
print(s.plusOne(case3)) # [1,0]