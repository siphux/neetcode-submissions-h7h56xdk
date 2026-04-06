class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(pos, spd) for pos, spd in zip(position, speed)]
        pair.sort(reverse=True, key = lambda x: x[0])
        for pos, spd in pair:
            stack.append((target-pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)