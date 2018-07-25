# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        d = {}
        for num in numbers:
            if not d.has_key(num):
                d[num] = 0
            else:
                duplication[0] = num
                return True
        return False
