# Solved using brute force (O(n^2) time complexity) – works, but not very efficient.
# A hash map (dictionary) approach can solve this in O(n) time, which is faster for large inputs.

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        