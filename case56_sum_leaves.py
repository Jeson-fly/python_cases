# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29  12:59
@Author : lining
@email：lining01@tuyooganme.com
@desc: 二叉树叶子结点之和
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def dfs(self, root, p):
        if root is None:
            return
        if root.left == None and root.right == None:
            p.append(root.val)
        self.dfs(root.right, p)
        self.dfs(root.left, p)

    def leaf_sum(self, root):
        tmp = []
        self.dfs(root, tmp)
        return sum(tmp)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    solution = Solution()
    res = solution.leaf_sum(root)
    print(res)