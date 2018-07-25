# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ''
        numbers = list(map(str, numbers))
        # cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
        numbers.sort(cmp=lambda x, y:cmp(x+y, y+x))
        return '0' if numbers[0]==0 else ''.join(numbers)
