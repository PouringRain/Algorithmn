# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        if left:
            while p.right:
                p = p.right
            p.right = pRootOfTree
            pRootOfTree.left = p
        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left =  pRootOfTree
        return left if left else pRootOfTree
