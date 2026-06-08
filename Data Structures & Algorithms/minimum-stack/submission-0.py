class MinStack:

    def __init__(self):
        self.stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum: int = float('inf')
        for num in self.stack: 
            if num < minimum: 
                minimum = num
        
        return minimum
