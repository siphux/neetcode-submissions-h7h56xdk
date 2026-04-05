class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top_stack = stack.pop() if len(stack) > 0 else -1
                if top_stack != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not len(stack)  
