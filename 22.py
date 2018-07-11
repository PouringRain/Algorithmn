# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        stack = [pRoot]
        flag = 1
        res = []
        while stack:
            subnode = []
            tmp = []
            for node in stack:
                tmp+=[node.val]
                if node.left:
                    subnode.append(node.left)
                if node.right:
                    subnode.append(node.right)
            if flag%2==0:
                tmp.reverse()
            flag+=1
            stack = subnode[:]
            res.append(tmp)
            
        return res
