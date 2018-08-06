# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 符号出现过，小数点出现过，E出现过
        sign, baby_point, hasE = False, False, False
        for i, c in enumerate(s):
            if c=='E' or c=='e':
                if i==len(s)-1: return False
                if hasE: return False
                hasE = True
            elif c=='+' or c=='-':
                if sign and s[i-1]!='E' and s[i-1]!='e':
                    return False
                if not sign and i>0 and s[i-1]!='E' and s[i-1]!='e':
                    return False
                sign = True
            elif c=='.':
                if baby_point or hasE:
                    return False
                baby_point = True
                
            elif c>'9' or c<'0': return False
            
        return True
