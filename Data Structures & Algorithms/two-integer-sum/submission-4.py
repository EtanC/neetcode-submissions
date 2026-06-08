class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        # for every number, check all consequent number to see if they add up to the target 

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        