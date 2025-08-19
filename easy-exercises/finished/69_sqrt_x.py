class Solution:
    def mySqrt(self, x: int) -> int:
        total = 0
        count = 0
        while(True):
            count += 1
            total = count * count
            if total > x: break
        return count - 1
    
s = Solution()

case1_x = 4
print(s.mySqrt(case1_x)) # 2

case2_x = 8
print(s.mySqrt(case2_x)) # 2