# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 堆排序
        if len(tinput)<k: return []
        heap = []
        ret = []
        for i in range(len(tinput)):
            heappush(heap, tinput[i])
        for i in range(k):
            ret.append(heappop(heap))
        return ret
