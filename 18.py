# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 打印螺旋矩阵
        if matrix == []: return []
        row = len(matrix)
        col = len(matrix[0])
        res = []
        # if row == 1 or col == 1:
        #     for i in range(row):
        #         for j in range(col):
        #             res.append(matrix[i][j])
        #     return res

        sx, ex, sy, ey = 0, row - 1, 0, col - 1
        while sx <= ex and sy <= ey:
            for i in range(sy, ey + 1):
                res.append(matrix[sx][i])
            sx += 1
            for i in range(sx, ex + 1):
                res.append(matrix[i][ey])
            ey -= 1
            for i in range(ey, sy - 1, -1):
                res.append(matrix[ex][i])
            ex -= 1
            for i in range(ex, sx - 1, -1):
                res.append(matrix[i][sy])
            sy += 1

        return res[:row * col]
