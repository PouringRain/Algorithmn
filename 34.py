# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        lenth = len(array)
        if lenth==1: return array[0]
        dp = [0]*lenth
        dp[0] = array[0]
        for i in range(1, lenth):
            # dp表示以A[i]结尾的最大连续字串的值
            dp[i] = max(dp[i-1]+array[i], array[i])
        return max(dp)
