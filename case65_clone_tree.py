#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/30 23:53
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 克隆二叉树
"""

from utils.list_node import TreeNode


class Solution:
    def clone_tree(self, root: TreeNode):
        if root is None:
            return None
        clone_root = TreeNode(root.val)
        clone_root.left = self.clone_tree(root.left)
        clone_root.right = self.clone_tree(root.right)
        return clone_root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    res = solution.clone_tree(root)
    # while res:
    # print(res.val)
    print(res.val)
    print(res.left.val)
    print(res.right.val)
