# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1 or number==0:
            return 1
        if number==2: 
            return 2
        ans = 0
        for i in range(number):
            ans+=self.jumpFloorII(i)
        return ans
