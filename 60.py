# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # base: float.   exponent: int
        if exponent==0: return 1
        ret = 1
        for i in range(abs(exponent)):
            ret *= base
        return ret if exponent>0 else 1/ret
    
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, n):
        # write code here
        ret, exp = 1, -1
        cur = base # 当前
        if n>0: exp = n
        elif n==0: return 1
        else: exp = -n
        while exp:
            if exp&1==1: 
                ret *= cur
            cur *= cur
            exp>>=1
        return ret if n>0 else 1/ret
        
