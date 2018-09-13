# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        def backtrack(matrix, i, j, curlen, path, mark):
            # print(mark)
            if i >= 0 and i < rows and j >= 0 and j < cols and matrix[i][j] == path[curlen] and mark[i][j]:
                if curlen == len(path) - 1:
                    if matrix[i][j] == path[curlen]:
                        return True
                    else:
                        return False

                mark[i][j] = False  # false是访问过了
                # 四个方向
                if backtrack(matrix, i - 1, j, curlen + 1, path, mark) or \
                        backtrack(matrix, i + 1, j, curlen + 1, path, mark) or \
                        backtrack(matrix, i, j - 1, curlen + 1, path, mark) or \
                        backtrack(matrix, i, j + 1, curlen + 1, path, mark):
                    return True
                mark[i][j] = True
            return False

        mark = [[1 for i in range(cols)] for j in range(rows)]
        m = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                m[i][j] = matrix[i * cols + j]
        for i in range(rows):
            for j in range(cols):
                if backtrack(m, i, j, 0, path, mark):
                    return True
        return False

a = Solution()
print(a.hasPath('ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS',5,8,"SGGFIECVAASABCEHJIGQEM"))
