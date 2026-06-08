class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        // brute force
        // for every num, just loop through the rest to see if they add up?
        for (let i = 0; i < numbers.length - 1; i++) {
            for (let j = i + 1; j < numbers.length; j++) {
                if (numbers[i] + numbers[j] === target) {
                    return [i + 1, j + 1]
                }
            }
        }
    }
}
