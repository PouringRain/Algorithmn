# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        #dp[i] = dp[i-1]+dp[i-2]
        if number==0 or number==1 or number==2:
            return number
        dp = [1, 2]
        for i in range(2, number):
            dp.append(dp[i-1]+dp[i-2])
        
        return dp[-1]
