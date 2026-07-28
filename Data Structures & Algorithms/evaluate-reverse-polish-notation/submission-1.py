class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
                continue
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    stack.append(stack.pop() - stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    stack.append(stack.pop() / stack.pop())
        return stack.pop()