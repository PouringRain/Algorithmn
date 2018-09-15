# ac

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def iqiyi_1(m, n):
    pass



# ******************************结束写代码******************************

line = input().strip().split()
# n种食物，m天，第p种
n, m ,p = int(line[0]), int(line[1]), int(line[2])

a = list(map(int, input().strip().split()))
for i in range(m):
    line = input().strip().split()
    trade = line[0]
    num = int(line[1])
    if trade=='A':
        a[num-1]+=1
    else:
        a[num-1]-=1

ret = 1
for i in range(n):
    if a[i]>a[p-1]:
        ret+=1
print(str(ret))
