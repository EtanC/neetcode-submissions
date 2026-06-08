class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longest = 0;
        let curr = 1;

        const newSet = new Set(nums);
        const count = [...newSet].sort((a, b) => a - b);

        for (let i = 0; i < count.length; i++) {
            if (count[i - 1] + 1 === count[i]) {
                curr++;
            } else {
                longest = Math.max(curr, longest);
                curr = 0;
            }
            longest = Math.max(curr, longest);
        }
        return longest;
    }
}
