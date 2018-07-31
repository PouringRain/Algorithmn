# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        p = pHead
        q = ListNode(0)
        while p:
            new = ListNode(p.val)
            tmp = q.next
            q.next = new
            q.next.next = tmp
            p = p.next
        return q.next
        
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # Solution2: 递归
        if not pHead or not pHead.next: 
            return pHead
        p = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return p
