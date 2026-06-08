class Solution:
    def isValid(self, s: str) -> bool:
        mapping: dict[str, str] = {
            "}" : "{", 
            "]" : "[", 
            ")" : "(", 
        }
        stack: list[str] = []
        for i in range(len(s), 0):
            if mapping[s[i]]:
                stack.add(s[i])
        
        for i, j in enumerate(stack):
            if s[i] != mapping[j]:
                return False
        
        return True
