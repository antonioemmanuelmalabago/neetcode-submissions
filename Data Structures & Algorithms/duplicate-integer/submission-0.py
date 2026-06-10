# Goal: Identify if any value appears more than once
# Algorithm:
# 1. Add all elements to a set.
# 2. Compare length of given list to set.
# 3. Return true if value returns more than once.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integerSet = set()

        for i in nums:
            integerSet.add(i)
        
        return not (len(nums) == len(integerSet))
         