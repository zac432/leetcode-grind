# 125. Valid Palindrome

**Difficulty:** Easy  
**Topic:** Strings, Two Pointers  
**Platform:** LeetCode

---

## Problem Statement

A phrase is a palindrome if, after:
1. Converting all uppercase letters into lowercase letters, and  
2. Removing all non-alphanumeric characters  

it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

---

### Examples

**Example 1:**

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


**Example 2:**

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


**Example 3:**
Input: s = " "
Output: true
Explanation: After cleaning, the string is empty "" which is a palindrome.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Approach

### Method 1: String Filtering + Reverse Check
1. Remove all non-alphanumeric characters from `s`.
2. Convert the cleaned string to lowercase.
3. Compare it with its reverse.
4. Return `True` if they are the same, otherwise `False`.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

### Method 2: Two Pointers (More Memory-Efficient)
1. Use two pointers: one at the start and one at the end.
2. Move inward, skipping non-alphanumeric characters.
3. Compare lowercase characters at both ends.
4. If all match, return `True`.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Pseudocode (Method 1)
function isPalindrome(s):
clean = ""
for each char in s:
if char is alphanumeric:
append lowercase(char) to clean
return clean == reverse(clean)