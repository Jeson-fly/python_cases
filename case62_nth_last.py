#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/30 0:11
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 倒数第n个节点（链表）
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def n_to_last(self, head, n):
        if head is None or n < 1:
            return None
        cur = head.next
        while cur is not None:
            cur.pre = head
            cur = cur.next
            head = head.next

        n -= 1
        while n > 0:
            head = head.pre
            n -= 1
        return head.val


if __name__ == '__main__':
    head = ListNode(3)
    head.next=ListNode(2)
    head.next.next=ListNode(1)
    head.next.next.next=ListNode(5)
    solution = Solution()
    res = solution.n_to_last(head,3)
    print(res)
