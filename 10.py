# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getHeight(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return 1+max(leftHeight, rightHeight)
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 平衡二叉树 |左子树高度-右子树高度|<=1
        if not pRoot: return True
        if abs(self.getHeight(pRoot.left)-self.getHeight(pRoot.right))<=1:
            return True
        else:
            return False
