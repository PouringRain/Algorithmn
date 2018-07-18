# -*- coding:utf-8 -*-
# 最low解法
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size==0: return []
        lenth = len(num)
        res = []
        for i in range(lenth-size+1):
            res.append(max(num[i:i+size]))
        
        return res
    
# solution 2
# -*- coding:utf-8 -*-
import collections
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # solution: 双向队列
        # 1. num[i]比前面的大，前面的都出队
        # 2. num[i]比前面的小，入队。若入队后len(滑窗)>size,队首出队
        q = collections.deque()
        ret = []
        for i, val in enumerate(num):
            print(q)

            if q:
                if len(q) >= size:
                    q.popleft()
                while q and q[0] <= val:
                    q.pop()

            q.append(val)
            if i+1 >= size:
                ret.append(q[0])

        return ret
