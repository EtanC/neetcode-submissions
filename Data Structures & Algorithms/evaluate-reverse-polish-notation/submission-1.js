class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const operator = ["+", "-", "*", "/"];
        let stack = [];

        for (char of tokens) {
            if (char in operator) {
                const char2 = stack.pop();
                const char1 = stack.pop();
                stack.push(this.evaluateNum(char, char1, char2));
            }
        }
    }

    evaluateNum(operator, a, b) {
        if (operator === "+") return a + b;
        if (operator === "+") return a + b;
    }
}
