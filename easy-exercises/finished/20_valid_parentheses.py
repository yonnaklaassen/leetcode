class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        open = ['(', '[', '{']
        closed = [')', ']', '}']
        stack = []
        for char in s:
            if char in open:
                stack.append(char)
            elif char in closed:
                if len(stack) != 0:
                    top_element = stack[-1]
                    if open.index(top_element) == closed.index(char):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

s = Solution()

case1 = "()"
print(s.isValid(case1)) # True

case2 = "()[]{}"
print(s.isValid(case2)) # True

case3 = "(]"
print(s.isValid(case3)) # False

case4 = "([])"
print(s.isValid(case4)) # True

case5 = "["
print(s.isValid(case5)) # False

case6 = "(("
print(s.isValid(case6)) # False

case7 = "]"
print(s.isValid(case7)) # False

case8 = "){"
print(s.isValid(case8)) # False

case9 = "([}}])"
print(s.isValid(case9)) # False