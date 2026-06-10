# Objective: Confirm if string of parenthesis is valid
# Condition: Same open and close bracket, correct order
# Algorithm:
# 1. Create an empty stack.
# 2. Dictionary to define relationship between open and close bracket.
# 3. Check if char is already in the stack
#   3.a. If yes, pop the stack
#   3.b. If not, add to stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(','}':'{',']':'['}

        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else: stack.append(c) 
        
        return not stack

                



