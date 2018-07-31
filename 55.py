# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        while n:
            cnt += n&1
            n = n >> 1&0x7fffffff
        return cnt
