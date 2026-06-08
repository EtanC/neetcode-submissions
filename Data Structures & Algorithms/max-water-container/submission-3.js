class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        // two pointer approach to shorten the search time 
        let i = 0;
        let j = heights.length - 1;
        let maxWater = 0;

        while (i < j) {
            maxWater = Math.max(maxWater, Math.min(heights[i], heights[j]) * (j - i));
            if (heights[i] < heights[j]) {
                i++;
            } else {
                j--;
            }
        }
        return maxWater;
    }
}
