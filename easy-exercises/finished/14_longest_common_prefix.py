from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        characters = [char for char in strs[0]]
        strs.pop(0)
        longest_common_prefix = ""
        for position, value in enumerate(characters):
             common = [w for w in strs if len(w) > position and w[position] == value]
             if len(common) ==  len(strs):
                 longest_common_prefix += value
             else:
                break
        return longest_common_prefix
    
s = Solution()

case1 = ["flower","flow","flight"]
print(s.longestCommonPrefix(case1)) # "fl"


case2 = ["dog","racecar","car"]
print(s.longestCommonPrefix(case2)) # ""

case3 = ["ab", "a"]
print(s.longestCommonPrefix(case3)) # "a"

