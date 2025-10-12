class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.matrix = matrix

        self.prefix = []
        for i in range(m):
            self.prefix.append([])
            for j in range(n):
                self.prefix[i].append(0)

        print(self.prefix)
        for i in range(m):
            for j in range(n):
                if j == 0 and i == 0:
                    self.prefix[i][j] = self.matrix[i][j]
                elif j == 0:
                    self.prefix[i][j] = self.prefix[i-1][j] + self.matrix[i][j]
                elif i == 0:
                    self.prefix[i][j] = self.prefix[i][j-1] + self.matrix[i][j]
                else:
                    self.prefix[i][j] = self.prefix[i][j-1] + self.prefix[i-1][j] - self.prefix[i-1][j-1] + self.matrix[i][j]
        print(self.prefix)





    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print("Pairs: (",row1,col1,") and (", row2,col2,")")
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        if row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        if col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        else:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2] - self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)