# Goal: Get the length of the longest substring w/o repetition
# Algorithm:
# 1. Expand the window until there is a duplicate
# 2. If duplicate, shrink the window until there is no duplicate
# 3. Track the length of longest substring
# Pitfalls:
# 1. When shrinking, remove the char from set
# 2. When encountered duplicate when expanding, the duplicate to be removed
# do not always located in left end, it can be within the window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            res = max(res, R - L + 1)
        
        return res
        
        