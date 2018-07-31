# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLinkLenth(self, head):
        if not head: return None
        size, p = 1, head
        while p.next:
            size+=1
            p = p.next
        return size
            
    def FindKthToTail(self, head, k):
        # write code here
        size = self.getLinkLenth(head)
        if size<k: return None
        end = size-k
        p = head
        while end:
            p = p.next
            end -= 1
        return p
        
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # Solution 2
        # p, q两个指针,p先走k步
        
        p = q = head
        while k:
            if p==None:
                return None
            p = p.next
            k -= 1
        while p:
            p = p.next
            q = q.next
        return q
