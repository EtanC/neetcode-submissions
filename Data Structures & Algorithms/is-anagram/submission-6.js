class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        const sCount = {};
        const tCount = {};

        for (const char in s) {
            sCount[char] = (sCount[char] || 0) + 1;
        }

        for (const char in t) {
            tCount[char] = (tCount[char] || 0) + 1;
        }

        for (const char in s) {
            if (sCount[char] !== tCount[char]) {
                return false;
            }
        }

        return true
    }
}
