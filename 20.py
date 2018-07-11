# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Symmetrical(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and t2:
            return t1.val==t2.val and self.Symmetrical(t1.left, t2.right) and self.Symmetrical(t1.right, t2.left)
        return False
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot: return True
        return self.Symmetrical(pRoot.left, pRoot.right)
