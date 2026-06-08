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
        const tCounter = {};

        for (const char of s) {
            sCount[char] = (sCount[char] || 0) + 1;
        }

        for (const char of t) {
            tCount[char] = (tCount[char] || 0) + 1;
        }

        for (const char in sCount) {
            if (sCount[char] !== tCount[char]) return false;
        }

        return true;
    }
}
