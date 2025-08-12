class Solution:
    def isPalindrome(self, x: int) -> bool:
     s = str(x) # converted input to string 
     if s == s[::-1]: #reversed string and checked if its equal so  if 121 is reversed it will be 121
        return True 
     else:
        return False
