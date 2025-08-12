class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the sentence into words, reverse each word, then join them back with spaces
        s = " ".join(f[::-1] for f in s.split())
        return s
