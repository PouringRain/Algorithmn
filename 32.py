# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d = {}
        queue = []
        for index, c in enumerate(s):
            if c not in d:
                queue.append(index)
                d[c] = 0
            d[c]+=1
            while queue and d[s[queue[0]]]>1:
                queue.pop(0)
        return queue[0] if queue else -1
