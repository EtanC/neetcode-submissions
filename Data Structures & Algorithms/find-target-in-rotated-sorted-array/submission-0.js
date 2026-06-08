class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        // brute force 
        let start = 0;
        let end = nums.length - 1;

        while (start < end) {
            if (nums[start] === target) {
                return start;
            } else if (nums[end] === target) {
                return end;
            }
            start++;
            end--; 
        }

        return -1;
    }
}
