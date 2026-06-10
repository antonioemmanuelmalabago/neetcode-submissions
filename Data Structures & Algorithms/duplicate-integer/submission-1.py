# Goal: Identify if any value appears more than once
# Algorithm:
# 1. Add all elements to a set.
# 2. Compare length of given list to set.
# 3. Return true if if len(set) < len(nums)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integerSet = set()

        for i in nums:
            integerSet.add(i)
        
        return len(integerSet) < len(nums)
         