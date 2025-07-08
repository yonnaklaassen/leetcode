class Solution:
    def isValid(self, s: str) -> bool:
        return self.checkForSameBrackets(s) and (self.checkForCorrectOrderSimple(s) or self.checkForCorrectOrderComplex(s))
    
    def checkForSameBrackets(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        curly_open_bracket_count = s.count("{")
        curly_closed_bracket_count = s.count("}")

        square_open_bracket_count = s.count("[")
        square_closed_bracket_count = s.count("]")

        round_open_bracket_count = s.count("(")
        round_closed_bracket_count = s.count(")")
    
        return (curly_open_bracket_count == curly_closed_bracket_count and
                square_open_bracket_count == square_closed_bracket_count and
                round_open_bracket_count == round_closed_bracket_count) and not (curly_open_bracket_count == 0 and
                                                                                 square_open_bracket_count == 0 and 
                                                                                 round_open_bracket_count == 0)
    
    def checkForCorrectOrderSimple(self, s: str) -> bool:
        open = ['(', '[', '{']
        closed = [')', ']', '}']
        if s[0] in closed or s[len(s) - 1] in open: return False

        pairs = []
        correctOrder = False

        for i in range(0, len(s), 2):
            pair = (s[i], s[i+1]) if i+1 < len(s) else (s[i],)
            pairs.append(pair)

        for pair in pairs:
            if pair[0] in open and pair[1] in closed:
                open_index = open.index(pair[0]) 
                closed_index = closed.index(pair[1])
                if open_index == closed_index:
                    correctOrder = True
                else:
                    correctOrder = False
            else:
                correctOrder = False
        return correctOrder
    
    def checkForCorrectOrderComplex(self, s: str) -> bool:
        open = ['(', '[', '{']
        closed = [')', ']', '}']
        return False
    

s = Solution()

case1 = "()"
print(s.isValid(case1)) # True

case2 = "()[]{}"
print(s.isValid(case2)) # True

case3 = "(]"
print(s.isValid(case3)) # False

case4 = "([])"
print(s.isValid(case4)) # True