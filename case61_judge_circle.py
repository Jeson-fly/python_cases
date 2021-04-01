#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/29 23:58
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 机器人回到原点
"""


class Solution:
    def __init__(self):
        self.dir_map = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0),
        }

    def judge_circle(self, direct: str):
        x = y = 0
        for item in direct:
            x += self.dir_map[item][0]
            y += self.dir_map[item][1]

        return x == 0 and y == 0


if __name__ == '__main__':
    dir = "RL"
    solution = Solution()
    res = solution.judge_circle(dir)
    print(res)
