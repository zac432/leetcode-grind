# Valid Parentheses

## Problem

Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

A string is valid if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.

### Examples

**Example 1**
Input: s = "()"
Output: True

**Example 2**
Input: s = "()[]{}"
Output: True

**Example 3**
Input: s = "(]"
Output: False

You can think of this problem like stacking dishes:

- Every time you get an opening bracket (`(`, `{`, `[`), you **put it on the stack**.
- Every time you get a closing bracket (`)`, `}`, `]`), you **check** if it matches the last dish (opening bracket) on top of the stack.
- If it matches, you remove the dish (pop from the stack).
- If it doesn’t match, the string is invalid.
