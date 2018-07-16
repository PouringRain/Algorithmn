# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        # 序列化
        def encode(node):
            if node:
                res.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                res.append('#')
        res = []
        encode(root)
        
        return ' '.join(res)
                
    def Deserialize(self, s):
        # write code here
        # 反序列化
        def decode():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = decode()
            node.right = decode()
            return node
        vals = iter(s.split())
        
        return decode()
