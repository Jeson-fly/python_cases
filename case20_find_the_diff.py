#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/4/1 0:14
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 计算两个字符串的不同
"""


class Solution:
    """

    """

    def find_the_difference(self, s, t):
        flag = 0
        for i in range(min(len(s), len(t))):
            flag += ord(s[i]) - ord(t[i])
        flag += ord(t[-1])
        flag = abs(flag)
        return chr(flag)


if __name__ == '__main__':
    s = "abcd"
    t = "abcd%"
    solution = Solution()
    res = solution.find_the_difference(s,t)
    print(res)