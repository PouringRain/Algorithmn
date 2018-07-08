# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        positive = 1; start = 0
        lenth = len(s)
        res = 0
        if lenth==0: return 0 #长度非法
        if s[0]=='-': positive=-1
        start = 1 if s[0]=='-' or s[0]=='+' else 0
        for i in range(start, lenth):
            if ord(s[i])<48 or ord(s[i])>57:
                return 0
            res = res*10 + ord(s[i])-48
        return res*positive
