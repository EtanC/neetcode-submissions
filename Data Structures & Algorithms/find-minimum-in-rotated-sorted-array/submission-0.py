class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force lol 
        nums.sort()
        return nums[0]