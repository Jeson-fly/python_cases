#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/30 0:27
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 链表
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Point:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
