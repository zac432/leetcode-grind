class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words, get the last word, and return its length
        return len(s.split()[-1])

        