# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 二叉搜索树的最近公共祖先
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or (root.val-p.val)*(root.val-q.val)<=0:
            return root
        elif root.val<p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
            
# 2. 反转链表
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
        
# 3. 快排
class Solution:
    def quickSort(self, nums, i, j):
        # write code here
        p, q = i, j
        if p>=q:
            return nums
        while p<q:
            key = nums[i]
            while p<q and nums[q]>=key:
                q-=1
            nums[p] = nums[q]
            while p<q and nums[p]<=key:
                p+=1
            nums[q] = nums[p]
        nums[p] = key
        self.quickSort(nums, i, p-1)
        self.quickSort(nums, q+1, j)

        return nums
