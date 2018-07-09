# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        
        a = s.split(' ')
        a.reverse() # reverse()直接对list操作，无返回值
        return ' '.join(a)
        
