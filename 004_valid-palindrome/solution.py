class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make a new string by:
        # 1. Going through each character `f` in the original string `s`
        # 2. Checking if `f` is alphanumeric (letter or number) with f.isalnum()
        # 3. If it is, convert it to lowercase with f.lower()
        # 4. Join all these filtered lowercase characters together with no spaces through "".join not " ".join
        s = "".join(f.lower() for f in s if f.isalnum())
        
        # Check if the cleaned string is the same forwards and backwards
        # s[::-1] creates a reversed copy of the string `s`
        # If they are equal, return True, else False
        return s == s[::-1]
