# Goal: Determine if two strings are anagrams
# Algorithms:
# 1. Compare the length of two strings. Return false if their lengths differ.
# 2. Create an empty frequency list for 26 letters.
# 3. Iterate through each index in len(s)
#   3.a. Add frequency for each character in s.
#   3.b. Subract frequency for each character in t.
# 4. Check if all elements in frequency list is zero.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        letterFreq = [0]*26

        for i in range(len(s)):
            letterFreq[ord(s[i]) - ord('a')] += 1
            letterFreq[ord(t[i]) - ord('a')] -= 1
        
        for l in letterFreq:
            if l != 0: return False
        
        return True