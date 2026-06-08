class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        j: int = len(s2) - 1
        while i != j: 
            if s2[i] != s2[j]:
                return False
            i += 1
            j -= 1 
        return True