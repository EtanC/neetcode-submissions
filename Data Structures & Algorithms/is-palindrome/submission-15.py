class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = " ".join(char for char in s if s.isalnum())
        i = 0 
        j = len(cleaned) - 1

        print(cleaned)

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False 
        
        return True