# 求数组的所有子集
# solution: 回溯

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(cur, i, nums, res):
            res.append(copy.deepcopy(cur))
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(cur, j+1, nums, res)
                cur.pop()
        dfs([], 0, nums, res)
        
        return res
