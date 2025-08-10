class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:  # it's a closing bracket
                # pop top if it exists, otherwise use a placeholder
                top = stack.pop() if stack else '#'
                if pairs[char] != top:
                    return False
            else:
                # it's an opening bracket
                stack.append(char)

        return not stack  # True if all brackets matched