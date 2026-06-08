class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        // brute force, go through every ehight and find the return the best one 
        let maxWater = 0;
        for (let i = 0; i < heights.length; i++ ) {
            for (let j = i; j < heights.length; j++) {
                maxWater = Math.max(maxWater, Math.min(heights[i], heights[j]) * (j - i));
            }
        }

        return maxWater
    }
}
