class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect

        row = bisect.bisect_left(matrix, target, key=lambda row: row[0]) - 1
        print(f"row: {row}")

        if row < 0:
            return False

        column = bisect.bisect_left(matrix[row], target)
        print(f"column: {column}")


        try:
            if matrix[row][column] == target:
                return True
            return False
        except:
            return False
            

        
        


