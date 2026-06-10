# Goal: Determine if string is palindrome, case-insensitive and only
# alphanumeric characters
# Algorithm:
# 1. Create left and right pointers. left=begin right=end
# 2. Use a loop to check the char at begin and end index
#   2.a. If they are the same, shrink the search space
#   2.b. If not, return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def isAlphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))
        