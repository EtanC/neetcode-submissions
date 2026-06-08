class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr: int = 0
        for i in nums:
            if i == curr:
                return True
            curr = i
        
        return False