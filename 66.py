# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV)!=len(popV):
            return False
        stack = []
        while popV:
            if pushV and popV[0]==pushV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
                
                    
