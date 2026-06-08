class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach, O(N^2). Going through each height and finding out whats the best one. 
        #max_water: int = 0
        #for i in range(len(heights)):
            #for j in range(i, len(heights)):
                #max_water = max(max_water, (min(heights[i], heights[j]) * (j - i)))
            
        #return max_water
        # reducing the amopunt we need to check by half. complexity becomes o(nlog)
        i: int = 0
        j: int = len(heights) - 1
        max_water: int = 0

        while i < j: 
            max_water = max(max_water, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
        return max_water
