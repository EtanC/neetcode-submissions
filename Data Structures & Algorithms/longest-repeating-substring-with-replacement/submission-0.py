class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using a dictionary to keep count of valid windows
        # a valid window is when len(window) - most_frequent_char <= k 

        count: dict[str, int] = {}
        left: int = 0
        result: int = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            most_frequent = max(count.values())
            
            while (right - left + 1) - most_frequent > k:
                count[s[left]] -= 1
                left += 1
                most_frequent = max(count.values())

            result = max(result, right - left + 1)

        return result

