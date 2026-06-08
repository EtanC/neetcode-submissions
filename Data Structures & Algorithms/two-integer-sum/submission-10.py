class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                second_target = target- nums[i] 
                if nums[j] == second_target and i != j:
                    return [i, j]
