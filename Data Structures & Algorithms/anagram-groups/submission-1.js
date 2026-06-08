class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const result = {};

        for (const s of strs) {
            const key = s.split('').sort().join('');
            if (!result[key]) result[key] = [];
            result[key].push(s);
        }
        return Object.values(result);
    
    }
}
