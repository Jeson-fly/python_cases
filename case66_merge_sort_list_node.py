#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/31 0:06
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 合并两个排序链表
"""

from utils.list_node import ListNode


class Solution:
    def merge_two_lists(self, list_node1, list_node2):
        list_root = ListNode(None)
        current_node = list_root
        while list_node1 and list_node2:
            if list_node1.val < list_node2.val:
                current_node.next = list_node1
                list_node1 = list_node1.next
            else:
                current_node.next = list_node2
                list_node2 = list_node2.next
            current_node = current_node.next
        while list_node1:
            current_node.next = list_node1
            list_node1 = list_node1.next
            current_node = current_node.next
        while list_node2:
            current_node.next = list_node2
            list_node2 = list_node2.next
            current_node = current_node.next
        return list_root.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(8)
    l2 = ListNode(2)
    l2.next = ListNode(4)

    solution = Solution()
    res = solution.merge_two_lists(l1, l2)
    while res:
        print(res.val)
        res = res.next
