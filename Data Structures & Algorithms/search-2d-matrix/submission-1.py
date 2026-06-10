# Objective: Search a target from 2D array
# Algorithm:
# 1. Find the row (range) where target can be found.
# 2. Find the target in the row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row, bot_row = 0, len(matrix) - 1

        while top_row <= bot_row:
            mid_row = top_row + (bot_row - top_row) // 2

            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break

        row = (top_row + bot_row) // 2
        
        left_p, right_p = 0, len(matrix[row]) - 1

        while left_p <= right_p:
            mid_p = left_p + (right_p - left_p) // 2

            if target > matrix[row][mid_p]:
                left_p = mid_p + 1
            elif target < matrix[row][mid_p]:
                right_p = mid_p - 1
            else:
                return True
        
        return False




