#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/26 23:50
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 合并两个有序数组
"""

from abc import ABCMeta, abstractmethod


class Solution(metaclass=ABCMeta):
    @abstractmethod
    def merge_array(self, l1: list, l2: list):
        """"""


class Method1Solution(Solution):
    def merge_array(self, list1, list2):
        i = j = 0
        tmp = list()
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                tmp.append(l1[i])
                i += 1
            else:
                tmp.append(l2[j])
                j += 1
        while i < len(l1):
            tmp.append(l1[i])
            i += 1
        while j < len(l2):
            tmp.append(l2)
            j += 1
        return tmp


if __name__ == '__main__':
    l1 = []
    l2 = []
    solution = Method1Solution()
    res = solution.merge_array(l1, l2)
    print(res)
