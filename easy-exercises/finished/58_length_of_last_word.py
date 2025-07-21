class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()
        index = len(split) - 1 
        return len(split[index].strip())
    
s = Solution()
case1 = "Hello World"
print(s.lengthOfLastWord(case1)) # 5

case2 = "   fly me   to   the moon  "
print(s.lengthOfLastWord(case2)) # 4

case3 = "luffy is still joyboy"
print(s.lengthOfLastWord(case3)) # 6