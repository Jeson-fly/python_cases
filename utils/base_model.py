#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/27 9:37
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 接口
"""

from abc import ABCMeta, abstractmethod


# 解决方法接口
class Solution(metaclass=ABCMeta):
    @abstractmethod
    def handler(self, *args):
        """"""
