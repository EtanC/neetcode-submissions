class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const operator = ["+", "-", "*", "/"];
        let stack = [];

        for (const char of tokens) {
            if (operator.includes(char)) {
                const char2 = stack.pop();
                const char1 = stack.pop();
                stack.push(this.evaluateNum(char, char1, char2));
            } else {
                stack.push(parseInt(char));
            }
        }
        console.log(stack)
        return stack[0];
    }

    evaluateNum(operator, a, b) {
        if (operator === "+") return a + b;
        if (operator === "-") return a - b;
        if (operator === "*") return a * b;
        if (operator === "/") return Math.trunc(a / b);
    }
}
