# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29  12:51
@Author : lining
@email：lining01@tuyooganme.com
@desc: 寻找第二大的数
"""


class Solution:
    def second_max_num(self, l1: list):
        max_value = max(l1[0], l1[1])
        min_value = min(l1[0], l1[1])
        for i in range(2, len(l1)):
            if l1[i] > max_value:
                min_value = max_value
                max_value = l1[i]
            elif l1[i] > min_value:
                min_value = l1[i]
        return min_value


if __name__ == '__main__':
    solution = Solution()
    l1 = [1, 2, 3, 4, 5, 6]
    res = solution.second_max_num(l1)
    print(res)
