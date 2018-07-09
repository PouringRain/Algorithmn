# -*- coding:utf-8 -*-
# solution 1
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count=0
        for i in range(len(data)):
            if k==data[i]:
                count+=1
        return count
    
# solution 2
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 排序过的，可以二分查找、
        start, end = 0, len(data)-1
        cnt = 0
        while start<=end:
            mid = (start+end)//2
            if data[mid]==k:
                cnt+=1
                tmp = mid-1
                while tmp>=0 and data[tmp]==k:
                    cnt+=1
                    tmp-=1
                tmp = mid+1
                while tmp<=len(data)-1 and data[tmp]==k:
                    cnt+=1
                    tmp+=1
                break
            elif data[mid]<k:
                start=mid+1
            else: end = mid-1
                
        return cnt
