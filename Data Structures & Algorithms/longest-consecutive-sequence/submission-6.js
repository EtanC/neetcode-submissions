class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longest = 0;
        let curr = 0;

        const count = new Set(nums);
        sort(count)

        for (const i = 1; i < count.length; i++) {
            if (count[i - 1] + 1 === count[i]) {
                curr++;
            } else {
                longest = Math.max(curr, longest);
                curr = 0;
            }
        }
        return longest;
    }
}
