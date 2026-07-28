class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
                print(stack)
                continue
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '-':
                    tmp = stack.pop()
                    stack.append(stack.pop() - tmp)
                case '/':
                    tmp = stack.pop()
                    stack.append(int(stack.pop() / tmp))
            print(stack)
        return stack.pop()