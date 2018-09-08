# coding=utf-8
import sys


def wangyi_3(floor, ocuppy, line):
    # 倒香槟，好像挺简单。。
    deep = len(floor)
    k, v = line[1]-1, line[2]  # k层,倒入v体积
    def dfs(k, rest, deep, floor, ocuppy):
        if k==deep:
            if rest<floor[k]-ocuppy[k]:
                ocuppy[k]+=rest
            else:
                ocuppy[k] = floor[k]
            return
        if rest<=floor[k]-ocuppy[k]:
            ocuppy[k] += rest
            return
        else:
            ocuppy[k] = floor[k]
            h = floor[k]-ocuppy[k]
            dfs(k+1, rest-h, deep, floor, ocuppy)
    dfs(k, v, deep, floor, ocuppy)
    return ocuppy

if __name__ == "__main__":
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    line = list(map(int, line.split()))
    n, m = line[0], line[1]
    floor = [] # 存每层容积
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    line = list(map(int, line.split()))
    ret = []
    ocuppy = [0]*n
    for i in range(n):
        floor.append(line[i])
    for i in range(m):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        line = list(map(int, line.split()))
        if line[0] == 1:
            # 查询
            ret.append(ocuppy[line[1]-1])
        else:
            ocuppy = wangyi_3(floor, ocuppy, line)
    for i in range(len(ret)):
        print(ret[i])
