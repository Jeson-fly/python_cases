# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29  19:14
@Author : lining
@email：lining01@tuyooganme.com
@desc: 判断尾数(使用递归算法dfs)
"""


def judge_the_last_number(s1):
    if len(s1) == 1:
        return 1
    if len(s1) == 2 and s1 in ["10", "11"]:
        return 2
    if s1[0] == "0":
        return judge_the_last_number(s1[1:])
    elif s1[:2] in ["10", "11"]:
        return judge_the_last_number(s1[2:])


s1 = "111110"
res = judge_the_last_number(s1)
print(res)
print(2 > (1 << 2))

