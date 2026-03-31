class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for i in range(iterations):
            df = 2*x
            x -= learning_rate * df
        return round(x, 5)