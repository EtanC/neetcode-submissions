class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = 0
        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(i, len(nums)):
                if nums[j] == remaining:
                    return [i, j]