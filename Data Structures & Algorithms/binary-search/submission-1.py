# Objective: Create efficient binary search method
# Algorithm:
# 1. Create left and right pointer
# 2. Implement binary search loop (condition: l <= r)
#       2.a. Calculate middle index
#       2.b. Compare number in middle to target
#           - If target > number: take right half search space
#           - If target < number: take left half search space
#           - If target found: return the index
# 3. Return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target > nums[m]: l = m + 1
            elif target < nums[m]: r = m - 1
            else: return m

        return -1
        