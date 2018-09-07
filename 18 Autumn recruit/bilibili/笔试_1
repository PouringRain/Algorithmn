# 结果：过了50%   暂时不知道错误在哪
# coding:utf8
def bilibili_1(m):
    if m == []: return []
    row_ = len(m)
    col_ = len(m[0])
    ret = []

    ssx = 0
    eex = row_-1
    ssy = 0
    eey = col_-1
    while ssx <= eex and ssy <= eey:
        for k in range(ssy, eey + 1):
            ret.append(m[ssx][k])
        ssx += 1
        for k in range(ssx, eex + 1):
            ret.append(m[k][eey])
        eey -= 1
        for k in range(eey, ssy - 1, -1):
            ret.append(m[eex][k])
        eex -= 1
        for k in range(eex, ssx - 1, -1):
            ret.append(m[k][ssy])
        ssy += 1

    return ret[:row_ * col_]

if __name__=='__main__':
    r, c = input().split()
    r = int(r)
    c = int(c)
    m = [[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        line = input().split()
        line = list(map(int, line))
        for j in range(c):
            m[i][j] = line[j]
    line = input().split()

    ret = bilibili_1(m)
    s = ''
    for i in range(len(ret)):
        s += str(ret[i])+','
    print(s[:-1])
    # for i in range(len(ret)):
    #     if i!=len(ret)-1:
    #         print(str(ret[i])+','.strip())
    #     else:
    #         print(str(ret[i]).strip())

