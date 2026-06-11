class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: 
            return False

        rules = {
            ")": "(", 
            "}": "{", 
            "]": "[", 
        }
        stack = []

        for char in s: 
            if char in rules.values(): 
                stack.append(char)
            if char in rules.keys(): 
                if not stack or stack.pop() != rules[char]:
                    return False
        
        return len(stack) == 0