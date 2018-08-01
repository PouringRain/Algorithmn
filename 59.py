# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 空树不是任意一个树的子树
        ret = False
        if not pRoot2 or not pRoot1: 
            return False
        if pRoot1.val==pRoot2.val:
            ret = self.isT1hasT2(pRoot1, pRoot2)
        if not ret:
            ret = self.HasSubtree(pRoot1.left, pRoot2)
        if not ret:
            ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret
    def isT1hasT2(self, t1, t2):
        if t2==None: 
            return True
        if t1==None:
            return False
        if t1.val!=t2.val:
            return False
        return self.isT1hasT2(t1.left, t2.left) and self.isT1hasT2(t1.right, t2.right)
        
        
        
