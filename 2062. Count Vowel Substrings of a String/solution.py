class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}   
        counter = 0                          

        for i in range(len(word)):
            seen = set()  
            for j in range(i, len(word)):
                ch = word[j]
                if ch not in vowels:   
                    break
                seen.add(ch)
                if len(seen) == 5:     
                    counter += 1

        return counter