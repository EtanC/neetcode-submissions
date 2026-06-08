class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach, O(N^2). Going through each height and finding out whats the best one. 
        max_water: int = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                max_water = max(max_water, (min(heights[i], heights[j]) * (j - i)))
            
        return max_water
