# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i]>rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]
            
        
 # 稍微快一点的方法： 551ms
 # -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 二分查找
        lenth = len(rotateArray)
        if lenth == 0:
            return 0
        left, right = 0, lenth - 1
        while left <= right:
            mid = (left+right)/ 2
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[left]:
                right = mid
            else:
                left = mid
        #return rotateArray[0]
