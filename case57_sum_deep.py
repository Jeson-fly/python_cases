# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29  13:17
@Author : lining
@email：lining01@tuyooganme.com
@desc: 二叉树的某层节点之和
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None


class Solution:
    def level_sum(self, root, max_deep):
        p = []
        self.dfs(root, p, 1, max_deep)
        return sum(p)

    def dfs(self, root, p, deep, max_deep):
        if root is None or deep > max_deep:
            return
        if deep == max_deep:
            p.append(root.val)
        deep += 1
        self.dfs(root.left, p, deep, max_deep)
        self.dfs(root.right, p, deep, max_deep)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(9)

    deep = 3

    solution = Solution()
    res = solution.level_sum(root,deep)
    print(res)