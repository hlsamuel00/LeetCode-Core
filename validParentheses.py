'''
***Workflow Timestamps***
1. Make Sure You Understand the Problem
    * 
2. Design and Verify a Solution
    * 
3. Write the Code and Pass Test Cases
    * 
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = ['(', ')', '{', '}', '[', ']']

        for char in s:
            idx = parentheses.index(char)
            if idx & 1 == 0:
                stack.append(char)
            elif stack and stack[-1] == parentheses[idx - 1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0