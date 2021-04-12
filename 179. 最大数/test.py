# 输入：nums = [10,2]
# 输出："210"
# 示例 2：
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 示例 3：
#
# 输入：nums = [1]
# 输出："1"
# 示例 4：
#
# 输入：nums = [10]
# 输出："10"

import heapq


class Solution:
    @staticmethod
    def largest_number(nums) -> str:
        cache = []

        for num in nums:
            heap_num = (str(num) * 10)[:10]
            heapq.heappush(cache, (-int(heap_num), str(num)))

        res = ''
        while cache:
            res += heapq.heappop(cache)[1]

        return '0' if res[0] == '0' else res


if __name__ == '__main__':
    print(Solution().largest_number([3, 30, 34, 5, 9]))
