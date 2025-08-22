Given a string word, return the number of substrings of word that:
Consist only of vowels (a, e, i, o, u), and
Contain all five vowels at least once.
A substring is defined as a contiguous block of characters within the string.

# Example

Input:
word = "aeiouu"
Output:
2

# Explanation:

"aeiou" contains all 5 vowels → valid
"aeiouu" also contains all 5 vowels → valid
No other substring qualifies.

class Solution:
def countVowelSubstrings(self, word: str) -> int:

    vowels = {"a", "e", "i", "o", "u"}

# Creates a set of all vowels.

# Sets are great because:

# - You can quickly check if a character is a vowel (ch in vowels).

# - You can track unique vowels in a substring.

    counter = 0

# Will store the total number of valid substrings we find.

    for i in range(len(word)):
        # Outer loop: choose the start index of the substring.
     # We try every possible starting position in word.

        seen = set()
        # For each new start index i, we create a fresh empty set seen.
        # This tracks which vowels appear in the substring starting at i.

    for j in range(i, len(word)):
        # Inner loop: expand the substring to the right from i to j.
        # This way we check every substring starting at i.

        ch = word[j]
        # Current character in the substring.

        if ch not in vowels:
            # If the character is not a vowel, the substring is invalid from here on.
            # break stops the inner loop early — saves time and avoids invalid substrings.
            break

        seen.add(ch)
        # Add the vowel to the seen set.
        # If the vowel was already added, the set ignores duplicates.

        if len(seen) == 5:
        counter += 1
    return counter
