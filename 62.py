# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        if not self.minstack:
            self.minstack.append(node)
        if self.minstack[-1]<node:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(node)
        self.stack.append(node)
    def pop(self):
        # write code here
        self.minstack.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]
