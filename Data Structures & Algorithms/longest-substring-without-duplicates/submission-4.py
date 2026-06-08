class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force first
        # use a set, and a counter 
        # two pointer approach too? 
        longest: int = 0
        unique: set[char] = set()
        if len(s) < 2: 
            return 1
        for char in s:
            if char not in unique: 
                unique.add(char)
            else: 
                if len(unique) > longest: 
                    longest = len(unique)
                unique.clear()
                unique.add(char)

        return longest