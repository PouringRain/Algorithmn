# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.heap = [], []
    def Insert(self, num):
        # write code here
        # 前面最小堆（前n/2）,后面最大堆（后n/2）
        small, big = self.heap
        heappush(big, num)
        heappush(small, -heappop(big))
        if len(small)>len(big):
            heappush(big, -heappop(small))
            
    def GetMedian(self,_):
        # write code here
        small, big = self.heap
        if len(big)>len(small):
            return big[0]
        else:
            return (-small[0]+big[0])/2.0
