# problem 557. Reverse Words in a String III

# Problem Statement

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and the initial word order.

# Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

# Approach

Split the input string s into words by spaces.

Reverse each word’s characters individually.

Join the reversed words with a space to reconstruct the sentence.

Return the resulting string.
