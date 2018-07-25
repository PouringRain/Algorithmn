# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array==[[]]: return False
        row = len(array)
        col = len(array[0])
        for i in range(row):
            if array[i][0]==target:
                return True
            elif array[i][0]<target:
                for j in range(col):
                    if array[i][j]==target:
                        return True
            else: pass
        return False
