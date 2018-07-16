# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 前序+中序-->二叉树
        if not tin:
            return None
        rootVal = pre.pop(0)
        root = TreeNode(rootVal)
        rootIndex = tin.index(rootVal)
        root.left = self.reConstructBinaryTree(pre, tin[:rootIndex])
        root.right = self.reConstructBinaryTree(pre,tin[rootIndex+1:])
        
        return root
