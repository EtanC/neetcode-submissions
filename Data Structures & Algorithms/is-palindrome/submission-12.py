class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = " ".join(s for s in text if s.isalnum())
        i = 0 
        j = len(s)

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False 
        
        return True