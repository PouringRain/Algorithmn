# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A)<=1: return []
        B = [1]*len(A)
        for i in range(1, len(A)):
            B[i] = B[i-1]*A[i-1]
        tmp = 1
        for i in range(1, len(A))[::-1]:
            tmp *= A[i]
            B[i-1] *= tmp
        
        return B
