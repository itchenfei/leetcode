# 示例：
# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# [1,0,1,2,1,1,7,5]
# [0,1,0,1,0,1,0,1]

from copy import deepcopy


def max_satisfied(customers, grumpy, X):
    # 求原应有顾客
    origin_customers = 0
    for n, g in enumerate(grumpy):
        if g == 0:
            origin_customers += customers[n]

    # 求[0, k)区间可以挽回的顾客
    grumpy_customers = 0
    for n in range(X):
        if grumpy[n] == 1:
            grumpy_customers += customers[n]

    # 求每个k范围内可以挽回的顾客
    customers_len = len(customers)
    res = grumpy_customers
    left = 0
    right = X
    while right < customers_len:
        if grumpy[left] == 1:
            grumpy_customers -= customers[left]
        if grumpy[right] == 1:
            grumpy_customers += customers[right]
        res = max(res, grumpy_customers)
        left += 1
        right += 1
    return origin_customers + res


if __name__ == '__main__':
    import timeit

    start = timeit.default_timer()
    _customer = [1, 0, 1, 2, 1, 1, 7, 5]
    _grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    x = 3
    print(max_satisfied(_customer, _grumpy, x))
    print(timeit.default_timer() - start)
