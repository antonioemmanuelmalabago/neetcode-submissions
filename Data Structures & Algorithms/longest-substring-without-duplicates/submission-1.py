# Objective: Find the length of longest substring
# Condition: Substring has unique characters and must be contiguous
# Algorithm:
# 1. Create an empty list, and two pointers
# 2. Iterate through each character in string using r
#    2.a. Check if character in r is already in list.
#         If yes, change left pointer l += r
#    2.b. If no, increase right pointer r += 1
# 3. Return length of substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        res = 0

        for c in s:
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            r += 1
            res = max(res, r - l)
        
        return res





