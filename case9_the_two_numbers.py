#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/26 0:24
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 不重复的2个数
"""
import functools
import time


def ctime(func):
    # @functools.wraps
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("用时：%d秒",time.time() - start_time)
        return res

    return wrapper


class Solution:
    # @classmethod
    @ctime
    def the_two_numbers(self, a: list):
        tmp = {}
        for i in a:
            if i in tmp:
                tmp.pop(i)
            else:
                tmp[i] = None
        return list(tmp.keys())


if __name__ == '__main__':
    a = [1, 2, 5, 1]
    # s = Solution()
    # res = s.the_two_numbers(a)
    # print(res)
    ans=[0,0]
    for i in a :
        ans[0]=ans[0]^i
        print(ans)