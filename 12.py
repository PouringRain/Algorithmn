# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        a = s[:n][::-1]
        b = s[n:][::-1]
        return (a+b)[::-1]
