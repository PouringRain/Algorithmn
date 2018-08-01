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
