# 给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12

#  上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                print("i: {}, j: {}".format(i, j))
                print('self.preSum[{}][{}] = {}'.format(i, j+1, self.preSum[i][j+1]))
                print('self.preSum[{}][{}] = {}'.format(i + 1, j, self.preSum[i + 1][j]))
                print('self.preSum[{}][{}] = {}'.format(i, j, self.preSum[i][j]))
                print("matrix[i][j] = {}".format(matrix[i][j]))
                self.preSum[i + 1][j + 1] = self.preSum[i][j + 1] + self.preSum[i + 1][j]  - self.preSum[i][j] + matrix[i][j]
                for line in self.preSum:
                    print(line)
        for i in self.preSum:
            print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + self.preSum[row1][col1]


if __name__ == '__main__':
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    print(NumMatrix(matrix).sumRegion(2, 1, 4, 3))