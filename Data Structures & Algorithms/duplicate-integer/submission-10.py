class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setMap = set()
        for num in nums: 
            if not setMap: 
                setMap.append(num)
            else: 
                return True
        
        return False
