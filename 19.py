# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        # 中序遍历 左 根 右
        # 1. pNode==None
        if not pNode: return None
        # 2. 有右子树
        if pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        # 3. 无右子树，且该节点为父节点的左子树，下个节点为父节点
        p = pNode.next
        # 4. 无右子树，且该节点不是父节点的左子树，向上搜索
        while p and p.right==pNode:
            pNode = p
            p = p.next
        return p
