# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 摩尔投票法
        if not numbers: return 0
        cnt = 0
        val = None
        for num in numbers:
            if cnt==0:
                val=num
                cnt+=1
            elif val==num:
                cnt+=1
            else:
                cnt-=1
        return val if numbers.count(val)*2>len(numbers) else 0
