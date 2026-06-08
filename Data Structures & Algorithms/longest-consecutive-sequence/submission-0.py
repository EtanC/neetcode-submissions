class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force 
        # put it into a set, sort the set
        # iterate it through once 

        count = sorted(set(nums))
        longest = 0
        curr = 1

        for i in range(1, len(count)):
            if count[i - 1] + 1 == count[i]:
                curr += 1
            else:
                longest = max(curr, longest)
                curr = 1

        return max(longest, curr)

