class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for ch in s:
            balance += 1 if ch == 'R' else -1
            if balance == 0:
                count += 1
        return count
