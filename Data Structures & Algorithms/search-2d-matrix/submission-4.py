class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect

        row = bisect.bisect_left(matrix, target, key=lambda row: row[0]) - 1

        if row < 0:
            if matrix[row + 1][0] == target:
                return True
            return False

        if row != len(matrix) - 1:
            matrix[row].append(matrix[row+1][0])

        column = bisect.bisect_left(matrix[row], target)

        try:
            if matrix[row][column] == target:
                return True
            return False
        except:
            return False
