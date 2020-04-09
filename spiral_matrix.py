## Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
## https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: return []

        R, C = len(matrix), len(matrix[0])

        seen = [[False]*C for _ in matrix]
        result = []
        dr = [0, 1, 0, -1] # direction increment col
        dc = [1, 0, -1, 0]

        r = c = di = 0
        for i in range(R*C):
            result.append(matrix[r][c])
            seen[r][c] = True

            rn = r + dr[di]
            cn = c + dc[di]

            if 0 <= rn < R and 0<= cn < C and seen[rn][cn] == False:
                r, c = rn, cn
            else:
                di = (di + 1) % 4
                r = r + dr[di]
                c = c + dc[di]

        return result
