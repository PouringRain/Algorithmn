# level: medium  leetcode 82

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        count = {}
        p = head
        while p:
            if count.has_key(p.val):
                count[p.val]=1
            else:
                count[p.val]=0
            p = p.next
        new = ListNode(0)
        p = new
        p.next = head
        while p.next:
            q = p.next
            if count[q.val]==1:
                p.next = q.next
            else:
                p = p.next
        return new.next    
