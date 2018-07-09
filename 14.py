# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        count = {}
        for i in range(len(array)):
            if count.has_key(array[i]):
                count[array[i]]+=1
            else:
                count[array[i]] = 1
        res = []
        for k, v in count.items():
            if v==1:
                res.append(k)
                
        return res
