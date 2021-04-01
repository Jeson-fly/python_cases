#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/26 23:29
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 翻转一个3位数字,或者n位数
"""

from abc import ABCMeta, abstractmethod


# 方法接口
class Solution(metaclass=ABCMeta):
    def reverse_integer(self, num: int):
        """"""


class StrSolution(Solution):
    """
    字符串方法
    """

    def reverse_integer(self, num):
        assert isinstance(num, int), "num must be int"
        num = str(num)[::-1]
        return int(num)


class RoundSolution(Solution):
    """
    取余数的方法
    """

    def reverse_integer(self, num: int):
        res = list()
        while num > 0:
            res = list(map(lambda x: 10 * x, res))
            res.append(num % 10)
            num = num // 10

        return sum(res)


if __name__ == '__main__':
    a = 12345
    solution = StrSolution()
    solution = RoundSolution()
    res = solution.reverse_integer(a)
    print(res, type(a))
