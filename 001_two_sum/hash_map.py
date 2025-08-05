# Efficient hash map solution for LeetCode 1: Two Sum
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in m:
                return [m[complement], i]
            m[num] = i
