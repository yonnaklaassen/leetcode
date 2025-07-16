class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = str(x)
        reverse = input[::-1]
        return input == reverse

s = Solution()
case1 = 121
print(s.isPalindrome(case1)) #True

case2 = -121
print(s.isPalindrome(case2)) #False

case3 = 10
print(s.isPalindrome(case3)) #False
