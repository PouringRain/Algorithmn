# 一个正面全部朝上的硬币的矩阵，挨个翻硬币，每翻一下周围相邻的也都跟着翻，问最终几个正面朝下的
# AC
#coding=utf-8
import sys

def wangyi_1(row, col):
    if row==1 and col==1: return 1
    if row==1:
        return col-2
    if col==1:
        return row-2
    count = 0
    if row==2 or col==2:
        return 0
    count = 0

    
    return 0

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    ret = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        line = list(map(int, line.split()))

        row, col = line[0], line[1]
        # print(row, col)
        ret.append(wangyi_1(row, col))
    for i in range(len(ret)):
        print(ret[i])
        #5

        # 5
        # 1 14
        # 1 2
        # 3 1
        # 4 1
        # 2 2
