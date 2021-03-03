# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 输入: 2
# 输出: [0,1,1]
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
# [0, 1, 2,  3,   4,   5,   6,   7,   8,    9,    10,   11,   12]        2*5
# [0, 1, 10, 011, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100]  ... 10000

def count_bits(num):
    lst = []
    for n in range(num + 1):
        lst.append(bin(n).count('1'))
    return lst


if __name__ == '__main__':
    print(count_bits(5))