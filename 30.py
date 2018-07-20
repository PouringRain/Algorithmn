# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # index 是 第n个丑数的意思
        # 丑数:只包含质因子2、3和5的数,质因子有点关键了
        if index==0: return 0
        heap = []
        heappush(heap, 1)
        count = 1
        last = None
        while count<=index:
            cur = heappop(heap)
            # 若有重复的数。。
            while cur==last:
                cur = heappop(heap)
            heappush(heap, cur*2)
            heappush(heap, cur*3)
            heappush(heap, cur*5)
            count+=1
            last = cur
        return last
            
