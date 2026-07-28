class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o1 = int(tokens[0])
        o2 = int(tokens[1])

        for i in range(2, len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                o2 = int(tokens[i])
                continue
            match tokens[i]:
                case '+':
                    o1 += o2
                case '-':
                    o1 -= o2
                case '*':
                    o1 *= o2
                case '/':
                    o1 /= o2
        return o1