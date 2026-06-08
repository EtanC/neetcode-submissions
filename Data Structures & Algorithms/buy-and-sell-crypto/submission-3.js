class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        // brute force
        let maxProfit = 0; 
        for (let i = 0; i < prices.length - 1; i++) {
            for (let j = i + 1; j < prices.length; j++) {
                maxProfit = Math.max(prices[i] + prices[j], maxProfit);
            }
        }
        return maxProfit;
    }
}
