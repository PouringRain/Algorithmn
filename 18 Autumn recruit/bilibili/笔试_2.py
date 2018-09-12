# 有一个矩阵n*n的，里面都是数字，从左上角到右下角，只能向右和向下走，求最小相加数字和

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def minJiansu(m, n):
    big = float('inf')
    dp = [[big for i in range(n)] for j in range(n)]
    dp[0][0] = 2
    for i in range(n):
        for j in range(n):
            if i>0 and j>0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]
            if i==0 and j>0:
                dp[i][j] = dp[i][j-1]+m[i][j]
            if i>0 and j==0:
                dp[i][j] = dp[i-1][j]+m[i][j]

    # print(dp)

    return dp[-1][-1]



# ******************************结束写代码******************************

n = 3
m = [[2,3,4], [5,2,8], [3,1,7]]
for i in range(n):
    print(m[i])

print(minJiansu(m, n))
