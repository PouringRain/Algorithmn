# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p, q = pHead1, pHead2
        while p!=q:
            p = pHead2 if not p else p.next
            q = pHead1 if not q else q.next
        return p
