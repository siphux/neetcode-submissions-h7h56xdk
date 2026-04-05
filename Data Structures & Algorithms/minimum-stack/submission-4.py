class MinStack:

    def __init__(self):
        self.stack = []
        self.current_index = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_index += 1

    def pop(self) -> None:
        self.stack.pop()
        self.current_index -= 1

    def top(self) -> int:
        return self.stack[self.current_index - 1]

    def getMin(self) -> int:
        return min(self.stack)
