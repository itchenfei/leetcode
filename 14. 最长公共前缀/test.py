# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串""。
#
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""

# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        cache = strs[0]
        for i in range(len(strs)):
            inner = ''
            for s in zip(cache, strs[i]):
                if s[0] == s[1]:
                    inner += s[0]
                else:
                    break
            cache = inner
        return cache


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))