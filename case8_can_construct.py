#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/27 9:31
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 勒索信
"""

from utils.base_model import Solution


class DictSolution(Solution):
    def handler(self, ransom_note: str, magazine: str):
        """"""
        return self.can_construct(ransom_note, magazine)

    def can_construct(self, s1, s2):
        tmp = {}
        for s in s2:
            tmp[s] = tmp.get(s, 0) + 1
        for t in s1:
            if t not in tmp:
                raise ValueError("ransomNote is wrong")
            tmp[t] -= 1
            if tmp[t] < 0:
                return False
        return True


if __name__ == '__main__':
    s1 = "a"
    s2 = "aab"
    solution = DictSolution()
    res = solution.handler(s1, s2)
    print(res)