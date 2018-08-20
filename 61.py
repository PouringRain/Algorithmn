# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a, b = [], [] # a存奇数，b存偶数
        for i in range(len(array)):
            if array[i]&1==1:
                a.append(array[i])
            else:
                b.append(array[i])
        return a+b
