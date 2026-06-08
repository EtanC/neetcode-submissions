class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setMap = set()
        for num in nums: 
            if num not in setMap: 
                setMap.add(num)
            else: 
                return True
        
        return False
