# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)<2: return []
        product = float('inf') #储存乘积的最小值
        res = []
        p, q = 0, len(array)-1 # 双指针
        while p<q:
            if array[p]+array[q]==tsum:
                if product>array[p]*array[q]:
                    product = array[p]*array[q]
                    if res==[]:
                        res.append(array[p])
                        res.append(array[q])
                    else:
                        res[0], res[1] = array[p], array[q]
                p+=1; q-=1
            elif array[p]+array[q]<tsum:
                p+=1
            else:
                q-=1
                
        return res
