# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: return []
        ret = [root.val]
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    ret.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    ret.append(node.right.val)
        return ret
