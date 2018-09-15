#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

# AC
# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

def miantiaosort(start, end):
    lenth = len(start)
    for i in range(lenth-1):
        for j in range(i+1, lenth):
            if end[j]<end[i]:
                end[j], end[i] = end[i], end[j]
                start[j], start[i] = start[i], start[j]
    return

def iqiyi_2(start, end):
    lenth = len(start)
    cnt = 0
    for i in range(lenth):
        if i==0:
           cnt+=1
           last = end[i]
        if start[i]>=last:
            last = end[i]
            cnt+=1
    return cnt



# ******************************结束写代码******************************

n = int(input().strip())
start = [0]*n
end = [0]*n
for i in range(n):
    line = list(map(int, input().strip().split()))
    if line[0]>line[1]:
        line[0], line[1] = line[1], line[0]
    start[i] = line[0]
    end[i] = line[1]


miantiaosort(start, end)
print(str(iqiyi_2(start, end)))


