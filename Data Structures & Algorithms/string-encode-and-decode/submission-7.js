class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (!strs) return []
        return strs.join(":;") + ":;"
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if (!str) return []

        let curr = ""
        let result = []
        let count = 0

        while (count < str.length) {
            if (str[count] === ":" && str[count + 1] === ";") {
                result.push(curr)
                curr = ""
                count += 2
            } else {
                curr += str[count]
                count += 1
            }
        }

        return result
    }
}
