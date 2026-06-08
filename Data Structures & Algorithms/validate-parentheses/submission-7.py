class Solution:
    def isValid(self, s: str) -> bool:
        mapping: dict[str, str] = {
            "}" : "{", 
            "]" : "[", 
            ")" : "(", 
        }
        stack: list[str] = []
        for c in s: 
            if c in mapping: 
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else: 
                    stack.append(c)
        return True if not stack else False