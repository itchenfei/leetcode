# 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是 True 。


def is_toeplitz_matrix(matrix) -> bool:
    matrix_line_nums = len(matrix)
    matrix_per_line_nums = len(matrix[0])
    num = 0
    if matrix_line_nums == 1:  # 如果是只有[[1]]特殊情况
        return True
    while num < matrix_line_nums - 1:  # 避免边界错误：判断到倒数第二行就可以了
        matrix_num = matrix[num]
        matrix_num_next = matrix[num + 1]
        for n in range(matrix_per_line_nums - 1):
            num1 = matrix_num[n]
            num2 = matrix_num_next[n + 1]
            if num1 != num2:
                return False
        num += 1
    return True


if __name__ == '__main__':
    _matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    truth = is_toeplitz_matrix(_matrix)
    print(truth)
