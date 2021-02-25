# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]

# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109

def transpose(matrix):
    matrix_len = len(matrix)  # 矩阵长度
    matrix_line_len = len(matrix[0])  # 每一行长度
    rst = []
    for j in range(matrix_line_len):
        cache = []
        for i in range(matrix_len):
            cache.append(matrix[i][j])
        rst.append(cache)
    return rst


if __name__ == '__main__':
    _matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = transpose(_matrix)
    print(res)
