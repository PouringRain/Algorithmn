# 有个人喜欢住有邻居的房子，#_#_# _代表空闲的房子，也是有邻居的，求这种空最大值和最小值
# AC

# coding=utf-8
import sys


def wangyi_2(total, ocupy):
    ret = []
    ret.append(0) # 最小就是最小啦
    # _ #_ # _# _
    if ocupy<=1 or total == ocupy:
        ret.append(0)
        return ret
    rest = total-ocupy
    if rest>=ocupy:
        ret.append(ocupy-1)
    else:
        ret.append(rest)
    return ret



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ret = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        line = list(map(int, line.split()))

        total, ocupy = line[0], line[1]
        # print(row, col)
        ret.append(wangyi_2(total, ocupy))
    for i in range(len(ret)):
        print(str(ret[i][0])+' '+str(ret[i][1]))
