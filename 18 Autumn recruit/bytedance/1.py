# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers==[]: return False
        min_num = 14
        max_num = -1
        s = [0]*14
        for i in range(len(numbers)):
            s[numbers[i]]+=1
            if numbers[i]==0:
                continue
            if s[numbers[i]]>1:
                return False
            max_num = max(max_num, numbers[i])
            min_num = min(min_num, numbers[i])
        if max_num-min_num<5:
            return True
        else:
            return False
