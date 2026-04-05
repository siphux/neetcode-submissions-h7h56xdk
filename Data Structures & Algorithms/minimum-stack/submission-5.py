class MinStack:

    def __init__(self):
        # Primary stack to store values
        self.stack = []
        # min_stack stores the index of the minimum value in the stack
        self.min_stack = []
        # Current index pointer
        self.current_index = 0

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If min_stack is empty or new val is smaller than current min
        # push the current index. Otherwise, re-push the existing min's index.
        if not self.min_stack or val < self.stack[self.min_stack[-1]]:
            self.min_stack.append(self.current_index)
        else:
            self.min_stack.append(self.min_stack[-1])
        
        self.current_index += 1

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            self.current_index -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Access the minimum element via the stored index
        return self.stack[self.min_stack[-1]]