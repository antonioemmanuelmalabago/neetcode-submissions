# Goal: Return indices of two numbers from list that adds up to target
# Clues: list is sorted, O(1) 
# Algorithm:
# 1. Declare left and right pointers.
# 2. Get the numbers in current points and add them.
# 3. Compare the sum to target number.
#   3.a If sum > target, shift right pointer.
#   3.b If sum < target, shift left pointer.
#   3.c If sum = target, return [left+1, right+1]
# 4. Repeat step 2 until l < r;
# 5. Return empth array

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []
        
        