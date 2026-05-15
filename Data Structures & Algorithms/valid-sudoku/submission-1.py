class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkLine(line):
            count = set()
            for num in line:
                    if num in count and num != ".":
                        return False
                    count[num] = True

        for row in board:
            if checkLine(row) == False:
                return False

        columns = []
        for i in range(9):
            columns.append([row[i] for row in board])
        for c in columns:
            if checkLine(c) == False:
                return False
        del columns

        def split(l, n):
            return tuple((l[i * n:(i + 1) * n] for i in range(n)))

        sections = split(board, 3)
        boxes = list()

        for s in sections:
            currentBoxes = [list() for i in range(3)]
            for i, row in enumerate(s):
                for j, ngroup in enumerate(split(row, 3)):
                    currentBoxes[j].extend(ngroup)     
            boxes.extend(currentBoxes)
            
        print(boxes)
        for box in boxes:
            if checkLine(box) == False:
                return False

        return True