# Brute force solution for LeetCode 1: Two Sum
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
