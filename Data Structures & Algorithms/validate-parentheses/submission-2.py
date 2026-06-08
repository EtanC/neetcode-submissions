class Solution:
    def isValid(self, s: str) -> bool:
        mapping: dict[str, str] = {
            "}" : "{", 
            "]" : "[", 
            ")" : "(", 
        }
        stack: list[str] = []
        for i in range(len(s)):
            if s[i] not in mapping:
                stack.append(s[i])
            else:
                stack.remove(mapping[s[i]])
        return stack == []
            
