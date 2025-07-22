class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a = len(a) - 1
        index_b = len(b) - 1
        result_str = ""
        carry = 0
        while((index_a >= 0 or index_b >=0) or carry == 1):
            total = carry

            if index_a >=  0:
                total += int(a[index_a])
                index_a -= 1
            if index_b >= 0:
                total += int(b[index_b])
                index_b -= 1

            result_str += (str(total % 2))

            if total >= 2:
                carry = 1
            else:
                carry = 0
        return result_str[::-1]
    
s = Solution()
case1_a = "11"
case1_b = "1"
print(s.addBinary(case1_a, case1_b)) # "100"

case2_a = "1010"
case2_b = "1011"
print(s.addBinary(case2_a, case2_b)) # "10101"

