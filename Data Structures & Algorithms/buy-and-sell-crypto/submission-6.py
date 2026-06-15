class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force 
        result = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                temp = prices[j] - prices[i]
                result = max(result, temp)
        
        return result
