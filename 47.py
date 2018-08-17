# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ret = ''
        for i, c in enumerate(s):
            if c==' ':
                ret += '%20'
            else:
                ret += c
        return ret
