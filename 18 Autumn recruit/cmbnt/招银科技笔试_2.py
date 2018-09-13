# 编辑距离 

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def minDistance(m, row, col, n):
    if row==n-1 and col==n-1:
        return m[row][col]
    elif row==n-1:
        return minDistance(row, col+1)+m[row][col]
    elif col==n-1:
        return minDistance(row+1, col)+m[row][col]
    else:
        return m[0][0] + min(minDistance(m[row+1:,:], row+1, col, n), minDistance(m[:,col+1:], row, col+1, n))


    return m[-1][-1]

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
