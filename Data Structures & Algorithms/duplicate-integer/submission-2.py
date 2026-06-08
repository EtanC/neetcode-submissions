class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup: set = set(nums)
        return list(dup) != nums