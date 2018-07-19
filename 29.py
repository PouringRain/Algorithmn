# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i]>rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]
            
