#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/27 8:59
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 下一个更大的数（单调递减数列）
"""

from abc import ABCMeta, abstractmethod


# 接口
class Solution(metaclass=ABCMeta):
    @abstractmethod
    def next_greater_element(self, list1: list, list2: list):
        """"""


class DictSolution(Solution):
    """
    常规思路
    """

    def next_greater_element(self, list1: list, list2: list):
        """"""
        tmp = {}


class DecreaseSolution(Solution):
    """
    单调递减数列+字典方法方法
    """

    def next_greater_element(self, list1: list, list2: list):
        """"""
        answer = {}  # 存储数字的下一位最大数字
        stock = []  # 需要构建的单调递减数列
        for i in list2:
            while stock and stock[-1] < i:
                answer[stock[-1]] = i
                stock.pop()
            stock.append(i)
        for i in stock:
            answer[i] = -1
        for i in range(len(list1)):
            list1[i] = answer[list1[i]]
        return list1


def get_all_solutions():
    return [
        DictSolution,
        DecreaseSolution
    ]


def get_handler(method_num):
    solution_list = get_all_solutions()
    assert method_num < len(solution_list)
    solution = solution_list[method_num]
    return solution()


if __name__ == '__main__':
    list1 = [4, 1, 2]
    list2 = [1, 3, 4, 2]

    solution = get_handler(1)
    res = solution.next_greater_element(list1, list2)
    print(res)
