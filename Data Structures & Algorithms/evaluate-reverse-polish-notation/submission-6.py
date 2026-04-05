import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        
        
        stack = []

        for token in tokens:
            if token in operator_map:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "/":
                    res = int(operator_map[token](num1, num2))
                else:
                    res = operator_map[token](num1, num2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]