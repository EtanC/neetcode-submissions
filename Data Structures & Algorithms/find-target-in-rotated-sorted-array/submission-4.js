class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let low = 0;
        let high = nums.length - 1;

        while (low <= high) {
            const mid = Math.floor((low + high) / 2);

            if (nums[mid] === target) return mid; 
            
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && nums[mid] >= target) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (nums[high] >= nums[mid]) {
                if (nums[high] >= target && nums[mid] <= target) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
}
