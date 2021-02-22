# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.

# 输入：[1,2,2,3,1,4,2]
# 输出：6


def find_shortest_sub_array(nums):
    # 获取每个数字对应个数
    d = dict()
    for num in nums:
        if d.get(num, None):
            d[num] = d[num] + 1
        else:
            d[num] = 1
    # 获取最大个数
    max_times = max(v for v in d.values())
    # 获取连续子数组长度
    result_list = []
    cnt = 0
    left = right = 0
    point = 0
    for find_number, times in d.items():
        if times == max_times:  # find_number 为需要查找的数字
            while point < len(nums):
                if nums[point] == find_number:
                    if cnt == 0:
                        left = point
                        cnt += 1
                    if cnt != 0:
                        right = point
                point += 1
            result_list.append(right - left + 1)
            cnt = 0
            left = right = 0
            point = 0
    return min(result_list)


if __name__ == '__main__':
    array = [1, 2, 2, 3, 1, 4, 2]
    _cnt = find_shortest_sub_array(array)
    print(_cnt)
