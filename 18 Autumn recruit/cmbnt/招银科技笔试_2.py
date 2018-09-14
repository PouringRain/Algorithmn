# 编辑距离 

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0 for i in range(size2+1)] for j in range(size1+1)]
        
        for i in range(size2+1):
            dp[0][i] = i
        for i in range(size1+1):
            dp[i][0] = i
        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, 1+min(dp[i-1][j], dp[i][j-1]))
                    
        return dp[-1][-1]

  

# ******************************结束写代码******************************


# res = compareVersionNumber(v1, v2)
# line = input().strip().split()
n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    line = list(map(int, input().strip().split(',')))
    for j in range(n):
        m[i][j] = line[j]

print(minDistance(m, 0, 0, n))
