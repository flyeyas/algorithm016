# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
import collections
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.44%)
# Likes:    801
# Dislikes: 0
# Total Accepted:    166.2K
# Total Submissions: 329.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1:
# 
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#

# @lc code=start
'''
深度优先搜索：
把每个岛屿记录下来，然后夷为平地最后
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n= len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.DFSMarking(grid, i, j, n, m)
                    count+=1
        return count
    
    def DFSMarking(self, grid, i, j, n, m):
        if i<0 or j<0 or i>=n or j>=m or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.DFSMarking(grid, i-1, j, n, m)
        self.DFSMarking(grid, i+1, j, n, m)
        self.DFSMarking(grid, i, j-1, n, m)
        self.DFSMarking(grid, i, j+1, n, m)

'''
国际站代码，耗时较高
https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
map函数：
Python2 直接返回列表
Python3 返回迭代器
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


'''
广度优先搜索：
遍历到陆地为1的点，以此开始广度搜索
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count+=1
                    grid[i][j] = '0'
                    deques = collections.deque([(i,j)])
                    while deques:
                        ii, jj = deques.popleft()
                        for x, y in [(ii - 1, jj), (ii + 1, jj), (ii, jj-1), (ii, jj+1)]:
                            if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                                deques.append((x,y))
                                grid[x][y] = '0'
        return count
# @lc code=end

