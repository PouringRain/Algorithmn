# 结果：

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def compareVersionNumber(v1:str, v2:str):
    v1 = v1.split('.')
    v2 = v2.split('.')

    size1, size2 = len(v1), len(v2)
    lenth = min(size1, size2)
    for i in range(lenth):
        if v1[i]>v2[i]:
            return 1
        elif v1[i]<v2[i]:
            return -1
    if size1>size2:
        return 1
    elif size1<size2:
        return -1
    else:
        return 0


# ******************************结束写代码******************************


# res = compareVersionNumber(v1, v2)
line = input().strip().split()

res = compareVersionNumber(line[0], line[1])
print(str(res) + "\n")
