#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/30 0:26
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 链表求和
"""

from utils.list_node import ListNode


class Solution:
    def add_list(self, l1, l2):
        cur = ListNode(None)
        self.dfs(l1, l2, cur, 0)
        return cur.next

    def dfs(self, head1, head2, cur, tmp):
        if head1 is None and head2 is None and tmp == 0:
            return
        elif head1 is None and head2 is None and tmp == 1:
            cur.next = ListNode(1)
        elif head1 is None and head2:
            cur.next = ListNode((head2.val + tmp) % 10)
            tmp = (head2.val + tmp) // 10
            self.dfs(None, head2.next, cur.next, tmp)
        elif head1 and head2 is None:
            cur.next = ListNode((head1.val + tmp) % 10)
            tmp = (head1.val + tmp) // 10
            self.dfs(head1.next, None, cur.next, tmp)
        else:
            cur.next = ListNode((head1.val + head2.val + tmp) % 10)
            tmp = (head1.val + head2.val) // 10
            self.dfs(head1.next, head2.next, cur.next, tmp)


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(1)
    l1.next.next = ListNode(9)
    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(2)
    l2.next.next.next = ListNode(1)
    solution = Solution()
    res = solution.add_list(l1, l2)
    while res:
        print(res.val)
        res = res.next
