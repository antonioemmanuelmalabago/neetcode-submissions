# Goal: Determine if two strings are anagrams
# Algorithms:
# 1. Create a list with 26 zeros. Map each index to alphabet letter
# 2. Iterate through each character in 's' then add frequency 
# 3. Iterate through each character in 't' then subtract frequency
# 4. Check if frequency list elements are all zeros


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterFrequency = [0]*26

        for c in s:
            letterFrequency[ord('a') - ord(c)] += 1
        
        for c in t:
            letterFrequency[ord('a') - ord(c)] -= 1
        
        for l in letterFrequency:
            if l != 0:
                return False
        
        return True