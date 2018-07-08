# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        ans = 1
        if n==0: return 0
        if n==1 or n==2: return ans
        a = b = 1
        n = n-2
        while n>0:
            ans = a+b
            a, b = b, ans
            n-=1
        return ans
