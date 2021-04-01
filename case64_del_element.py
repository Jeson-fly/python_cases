#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/30 1:04
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 删除元素（原地删除）
"""


class Solution:
    def remove_element(self, A, elem):
        j = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j + 1


if __name__ == '__main__':
    A = [0, 4, 4, 0, 0, 2, 4, 4]
    elem = 4
    solution = Solution()
    res = solution.remove_element(A, elem)
    print(res)
