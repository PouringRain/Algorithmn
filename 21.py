# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        # 二叉树按行输出
        import Queue
        q = Queue.Queue()
        if not pRoot: return []
        q.put(pRoot)
        res = []
        while not q.empty():
            sub = []
            subqueue = Queue.Queue()
            while not q.empty():
                node = q.get()
                sub.append(node.val)
                if node.left:
                    subqueue.put(node.left)
                if node.right:
                    subqueue.put(node.right)
            res.append(sub)
            # 将新的节点加入
            while not subqueue.empty():
                node = subqueue.get()
                q.put(node)
                
        return res
