class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (!nums) {
            return 0;
        }
        
        let longest = 0;
        let curr = 1;

        const newSet = new Set(nums);
        const count = [...newSet].sort((a, b) => a - b);

        for (let i = 1; i < count.length; i++) {
            if (count[i - 1] + 1 === count[i]) {
                curr++;
            } else {
                longest = Math.max(curr, longest);
                curr = 1;
            }
            longest = Math.max(curr, longest);
        }
        return longest;
    }
}
