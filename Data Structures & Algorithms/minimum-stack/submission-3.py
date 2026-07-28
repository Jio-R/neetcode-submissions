class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = None
        self.minIndexes = []

    def push(self, val: int) -> None:
        if self.minNum == None or val <= self.minNum:
            self.minNum = val
            self.minIndexes.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minNum:
            del self.minIndexes[-1]
            if not self.minIndexes:
                self.minNum = None
            else:
                self.minNum = self.stack[self.minIndexes[-1]]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum
        
