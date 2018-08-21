# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node>root:
                break
            i+=1
        for node in sequence[i:-1]:
            if node<root:
                return False
        left = True
        if i>1: # 不大于1没得递归了
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if len(sequence)-i>2 and left:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
