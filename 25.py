# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
        self.ret = None
    def inTravel(self, root, k):
        if not root: return
        self.inTravel(root.left, k)
        self.count+=1
        if self.count==k:
            self.ret = root
        self.inTravel(root.right, k)
    def KthNode(self, pRoot, k):
        # write code here
        # 中序遍历
        self.inTravel(pRoot, k)
        return self.ret

    
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot: 
            
            node = self.KthNode(pRoot.left, k)
            if node: return node
            self.count += 1
            if k == self.count:
                return pRoot
            node = self.KthNode(pRoot.right, k)
            if node: return node
        return None
    
  # 非递归
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 非递归实现找到二叉搜索树的第k小的数
        if not pRoot: return None
        stack = []
        node = pRoot
        kthNode = None
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count+=1
            if count==k: 
                kthNode = node
            node = node.right
        return kthNode
