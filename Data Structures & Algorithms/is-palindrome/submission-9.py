class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = " ".join(join(char for char in text if char.isalnum()))
        i = 0 
        j = len(s)

        while i < j:
            if s[i] != s[j]:
                return False 
        
        return True