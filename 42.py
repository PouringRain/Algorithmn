# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return False
        numbers = sorted(numbers)
        distance = 0
        zeros = numbers.count(0)
        for i in range(zeros, len(numbers)-1):
            if numbers[i+1]-numbers[i]==0: return False
            if numbers[i+1]-numbers[i]>1:
                distance+=numbers[i+1]-numbers[i]-1
        return True if distance<=zeros else False
