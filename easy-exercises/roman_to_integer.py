import re
class Solution:

    ROMAN_NUMBERS = dict({
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    })

    EXCEPTIONS = dict({
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    })

    def romanToInt(self, s: str) -> int:
        sum = 0
        for key in self.EXCEPTIONS:
            x = re.findall(key, s)
            if len(x) != 0:
                for item in x:
                    s = s.replace(item, "")
                    sum += self.EXCEPTIONS[item]
        for char in s:
            sum += self.ROMAN_NUMBERS[char]            
        return sum
    


s = Solution()

case1 = "III"
print(s.romanToInt(case1)) # 3

case2 = "LVIII"
print(s.romanToInt(case2)) # 58

case3 = "MCMXCIV"
print(s.romanToInt(case3)) # 1994

case4 = "MCDLXXVI"
print(s.romanToInt(case4)) # 1476