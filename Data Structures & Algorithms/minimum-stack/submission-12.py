class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.current_index = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val < self.stack[self.minstack[-1]]:
            self.minstack.append(self.current_index)
        else:
            self.minstack.append(self.minstack[-1])
        self.current_index += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.current_index -= 1

    def top(self) -> int:
        return self.stack[self.current_index - 1]

    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
