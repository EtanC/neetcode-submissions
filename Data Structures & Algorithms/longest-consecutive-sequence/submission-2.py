class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force 
        # put it into a set, sort the set
        # iterate it through once 
        # this is o(nlogn) due to the sort

        num_set: set = set(nums)
        longest: int = 0

        for num in num_set: 
            if num - 1 not in num_set: 
                curr = 1
                while num + curr in num_set: 
                    curr += 1
                
                longest = max(curr, longest)
            
        return longest



