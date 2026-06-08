class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator: list[str] = ["+", "-", "*", "/"]
        stack: list[int] = []
        for char in tokens: 
            if char in operator: 
                num2: int = stack.pop()
                num1: int = stack.pop()
                stack.append(self.evaluate_num(char, num1, num2))
            else: 
                stack.append(int(char))
        
        return stack[0]
    
    def evaluate_num(self, operator: str, a: int, b: int) -> int: 
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(a / b)