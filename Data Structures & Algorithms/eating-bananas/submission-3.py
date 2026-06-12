class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # (sum(piles + k - 1) // k 
        low, high = 1, max(piles)

        while low < high: 
            k = (low + high) // 2
            hours_needed = sum(math.ceil(pile / k) for pile in piles)
            if hours_needed <= h: 
                high = k
            else: 
                low = k + 1
            
        return low