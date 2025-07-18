class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if needle in haystack: index = haystack.index(needle, 0, len(haystack))
        return index
    
s = Solution()

case1_haystack = "sadbutsad"
case1_needle = "sad"
print(s.strStr(case1_haystack, case1_needle)) # 0

case2_haystack = "leetcode"
case2_needle = "leeto"
print(s.strStr(case2_haystack, case2_needle)) # -1