# level: eazy. leetcode 142
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        while fast:
            fast=fast.next
            if slow==fast:
                return slow
            if fast==None: return None
            else:
                slow = slow.next
                fast = fast.next
        return None
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        meet = self.hasCycle(head)
        if meet!=None:
            p, q = head, meet.next
            while p!=q:
                p = p.next
                q = q.next
            return p
        else:
            return None
        
