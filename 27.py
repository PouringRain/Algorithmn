# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size==0: return []
        lenth = len(num)
        res = []
        for i in range(lenth-size+1):
            res.append(max(num[i:i+size]))
        
        return res
