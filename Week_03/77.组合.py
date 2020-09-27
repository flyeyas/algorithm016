# @before-stub-for-debug-begin
from python3problem77 import *
from typing import *
import copy
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (75.74%)
# Likes:    399
# Dislikes: 0
# Total Accepted:    106.3K
# Total Submissions: 140.3K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
'''
回溯算法是在一棵树上的深度优先遍历， 需要寻找所有可能的解，所有需要遍历
'''

# 没有剪枝

'''

'''
class Solution:
    def combine(self, n: int, k: int):
        res = []
        if k<=0 or n<k:
            return res
        path = []
        self.DFS(n, k, 1, path, res)
        return res
    
    def DFS(self,n:int ,k:int, index:int, path:list, res:list):
        if len(path) == k:
            res.append(copy.copy(path)) # 这里需要进行浅拷贝
            return
        for i in range(index, n+1):
            path.append(i)
            self.DFS(n,k,i+1,path,res)
            path.pop()


'''
优化：
当最后搜索的数字长度小于k - len(path)的时候，没有继续递归的必要了


'''
class Solution:
    def combine(self, n: int, k: int):
        res = []
        if k<=0 or n<k:
            return res
        path = []
        self.DFS(n, k, 1, path, res)
        return res
    
    def DFS(self,n:int ,k:int, index:int, path:list, res:list):
        if len(path) == k:
            res.append(copy.copy(path)) # 这里需要进行浅拷贝
            return
        for i in range(index, n-(k-len(path))+1+1):
            path.append(i)
            self.DFS(n,k,i+1,path,res)
            path.pop()


'''
python内置库
'''
# class Solution:
#     def combine(self, n, k):
#         return list(combinations(range(1, n+1), k))
        

'''
覃超老师说的光头哥的代码写法
https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
'''
class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
# @lc code=end

