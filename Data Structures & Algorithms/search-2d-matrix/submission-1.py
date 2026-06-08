class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search aka, search middle and determine whether up or down 
        # find middle row, if start > target, search in row - 1
        # if start > target and end < target, search in row 
        # else, row + 1
        # can do binary search again for the column operation 

        row, col = len(matrix), len(matrix[0])
        curr = row // 2

        while 0 <= curr < row:
            if matrix[curr][0] <= target <= matrix[curr][-1]: 
                break
            if matrix[curr][0] > target:
                curr -= 1
            else: 
                curr += 1
        print(curr)
        
        col_curr = col // 2
        while 0 <= col_curr < col:
            if matrix[curr][col_curr] == target:
                return True
            elif matrix[curr][col_curr] < target:
                col_curr += 1
            else:
                col_curr -= 1

        return False