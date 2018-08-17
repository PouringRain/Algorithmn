# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.d = {}
        self.q = []
    def FirstAppearingOnce(self):
        # write code here
        while self.q and self.d[self.q[0]]>1:
            self.q.pop(0)
        return self.q[0] if self.q else '#'
    def Insert(self, char):
        # write code here
        if self.d.has_key(char):
            self.d[char] += 1
        else:
            self.d[char] = 1
            self.q.append(char)
            
