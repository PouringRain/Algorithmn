# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root: return []
        ret = []
        def dfs(path, node, rest, ret):
            if not node.left and not node.right and (rest-node.val)==0:
                ret.append(path+[node.val])
            if node.left:
                dfs(path+[node.val], node.left, rest-node.val, ret)
            if node.right:
                dfs(path+[node.val], node.right, rest-node.val, ret)
        dfs([], root, expectNumber, ret)
        
        return ret
             
