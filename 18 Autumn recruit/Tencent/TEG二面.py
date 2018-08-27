# 1. 拓扑排序
# 时间复杂度 O(n+e) 输出n个顶点，去掉e个边，方法说对了，算错了复杂度，伤啊 --！
class Solution:
    def topSort(self, graph):
        # write code here
        in_degrees = dict((u, 0) for u in graph)
        print(in_degrees)
        vertex_num = len(graph)
        # 计算入度
        for k in graph:
            for c in graph[k]:
                in_degrees[c]+=1
        q = [u for u in in_degrees if in_degrees[u]==0]
        ret = []
        while q:
            node = q.pop()
            ret.append(node)
            for u in graph[node]:
                in_degrees[u]-=1
                if in_degrees[u] == 0:
                    q.append(u)

        if len(ret)==vertex_num:
            return ret
        else:
            return 'cant sort'



a = Solution()
print(a.topSort({'a':'bce', 'b':'d', 'c':'d', 'd':'', 'e':'cd'}))

# 2. 子矩阵的最大和
# solution: dp 时间复杂度 O(n^3)
# -*- coding:utf-8 -*-

class Solution:
    def maxSum(self, m):
        # write code here
        # m : List[List[]]
        if not m or len(m)==0 or len(m[0])==0:
            return 0
        row, col = len(m), len(m[0])
        ret = -float('inf')
        for i in range(row):
            for j in range(i, row):
                # i为首行
                sum = 0
                for k in range(0, col):
                    if i!=j:
                        m[i][k] = m[i][k] + m[j][k]

                    sum += m[i][k]
                    ret = max(ret, sum)
                    sum = 0 if sum<0 else sum

        return ret


a = Solution()
print(a.maxSum([[-90, 48, 78], [64, -40, 64], [-81, -7, 66]]))
