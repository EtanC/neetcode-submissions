class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let low = 0;
        let high = nums.length - 1;
        let mid = Math.trunc((low + high) / 2);

        while (low <= high) {
            mid = Math.trunc((low + high) / 2);
            if (nums[mid] > target) {
                high -= 1;
            } else if (nums[mid] < target) {
                low -= 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
