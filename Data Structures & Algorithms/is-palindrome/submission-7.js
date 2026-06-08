class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLowerCase().split(' ').join("");
        let i = 0;
        let j = s.length;

        while (i < j) {
            if (s[i] !== s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
