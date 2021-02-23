# 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是 True 。

import time


def is_toeplitz_matrix(matrix):
    line_nums = len(matrix)  # 多少行
    per_line_nums = len(matrix[0])  # 每行多少个
    col = 0
    while col < per_line_nums - 1:
        line = 0
        while line < line_nums - 1:
            if matrix[line][col] != matrix[line + 1][col + 1]:
                return False
            line += 1
        col += 1

    return True


if __name__ == '__main__':
    _matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    truth = is_toeplitz_matrix(_matrix)
    print(truth)