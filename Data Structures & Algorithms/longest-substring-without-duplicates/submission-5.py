class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force first
        # use a set, and a counter 
        # two pointer approach too? 
        charSet: set[char] = set()
        left: int = 0
        result:int = 0
        for right in range(len(s)):
            while s[right] in charSet: 
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, len(charSet))
        return result