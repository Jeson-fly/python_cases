# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29  19:29
@Author : lining
@email：lining01@tuyooganme.com
@desc: 两个字符串是变为串
"""


class Solution:
    def anagram(self, s1, s2):
        s1_map = {}
        for item in s1:
            s1_map[item] = s1_map.get(item, 0) + 1

        for item in s2:
            if item not in s1_map:
                return False
            s1_map[item] -= 1

        for k, v in s1_map.items():
            if v < 0:
                return False
        return True


if __name__ == '__main__':
    s = "abcd"
    t = "dcbaaaaa"
    solution = Solution()
    res = solution.anagram(s, t)
    print(res)
