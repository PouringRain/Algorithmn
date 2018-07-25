# -*- coding:utf-8 -*-
class Solution:
    def count(self, num):
        cnt = 0
        while num>0:
            k = num%10 # 余数
            if k==1: cnt+=1
            num /= 10
        return cnt
    
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ret = 0
        for num in range(1, n+1):
            ret += self.count(num)
        return ret
