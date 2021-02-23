# 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是 True 。


def is_toeplitz_matrix(matrix) -> bool:
    for line in range(len(matrix) - 1):
        if matrix[line][:-1] != matrix[line + 1][1:]:
            return False
    return True


if __name__ == '__main__':
    _matrix = [[1, 2, 3, 4],
               [5, 1, 2, 3],
               [9, 5, 1, 2]]
    truth = is_toeplitz_matrix(_matrix)
    print(truth)
