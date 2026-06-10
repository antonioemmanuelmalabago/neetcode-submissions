# Goal: Identify if any value appears more than once
# Algorithm:
# 1. Iterate through each elements of the list
#   1.a Simulataneously check if current element is already in set
#       - If present, return true
#       - If not, add the element to the set

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integerSet = set()

        for num in nums:
            if num in integerSet:
                return True
            integerSet.add(num)
        
        return False