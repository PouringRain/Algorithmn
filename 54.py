# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        # 回溯
        ret = []
        def dfs(cs, ci, ret):
            if ci==len(cs)-1 and ''.join(cs) not in ret:
                ret.append(''.join(cs))
            else:
                for i in range(ci, len(cs)):
                    cs[ci], cs[i] = cs[i], cs[ci]
                    dfs(cs, ci+1, ret)
                    cs[ci], cs[i] = cs[i], cs[ci]
        cs = list(ss)
        dfs(cs, 0, ret)
        
        return sorted(ret)
