# @before-stub-for-debug-begin
from python3problem64 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.57%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    151.4K
# Total Submissions: 224K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
'''
官方题解
设置一个空的矩阵，矩阵中（i,j）存放走到当前位置最短路径的值，然后把每次计算出的值填充到对应的位置
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]

'''
不需要建立 dp 矩阵浪费额外空间，直接遍历 grid[i][j] 修改即可。这是因为：grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]；原 grid 矩阵元素中被覆盖为 dp 元素后（都处于当前遍历点的左上方），不会再被使用到。

链接：https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        for index in range(1,rows):
            grid[index][0] += grid[index-1][0]
        
        for index in range(1, columns):
            grid[0][index] += grid[0][index-1]

        for i in range(1,rows):
            for j in range(1,columns):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        
        return grid[rows - 1][columns - 1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        # 填充行, 每一行的索引是1的元素
        for index in range(1, rows):
            grid[index][0]+= grid[index-1][0]

        #填充列, 每一列的索引是1的元素
        for index  in range(1, columns):
            grid[0][index] += grid[0][index-1]
        
        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]
# @lc code=end

