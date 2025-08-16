class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            x1 = int(num1[i]) if i >= 0 else 0
            x2 = int(num2[j]) if j >= 0 else 0
            total = x1 + x2 + carry
            carry = total // 10
            res.append(str(total % 10))
            i -= 1
            j -= 1

        return ''.join(res[::-1])


        