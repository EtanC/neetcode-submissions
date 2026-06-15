class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left, right = 0, 0
        max_result = 0
        for right in range(len(s)):
            while s[right] in result: 
                result.remove(s[left])
                left += 1
            result.add(s[right])
            max_result = max(max_result, len(result))
        return max_result