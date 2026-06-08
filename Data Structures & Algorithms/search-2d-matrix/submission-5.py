class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search aka, search middle and determine whether up or down 
        # find middle row, if start > target, search in row - 1
        # if start > target and end < target, search in row 
        # else, row + 1
        # can do binary search again for the column operation 

        rows, cols = len(matrix), len(matrix[0])

        lo, hi = 0, rows - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return False

        row = mid
        lo, hi = 0, cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False