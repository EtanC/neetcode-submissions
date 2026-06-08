class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = " ".join(char.lower() for char in s if char.isalnum())
        i = 0 
        j = len(cleaned) - 1

        print(cleaned)

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False 
            i += 1
            j -= 1
        
        return True