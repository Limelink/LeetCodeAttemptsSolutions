"""
LeetCode - 704. Binary Search
26.12.2022
"""

class Solution:
    def linear_search(self, nums: list[int], target: int) -> int:

        try:
            return nums.index(target)
        except ValueError:
            return -1

    def binary_search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
