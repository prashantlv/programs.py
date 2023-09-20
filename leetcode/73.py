# first

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        r,c = [],[]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.append(i) 
                    c.append(j)

        for i in range(rows):
            for j in range(cols):
                if i in set(r):
                    matrix[i][j] = 0
                if j in set(c):
                    matrix[i][j] = 0

