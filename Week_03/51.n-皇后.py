# @before-stub-for-debug-begin
# from python3problem51 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.09%)
# Likes:    613
# Dislikes: 0
# Total Accepted:    79.1K
# Total Submissions: 108.3K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例：
# 
# 输入：4
# 输出：[
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
# 
# 
#

# @lc code=start
'''
记住已经摆放好的皇后位置，摆放新的皇后位置时，检查新的皇后位置是否和旧的一个皇后在同一条横行、纵行或斜线上。
右斜线点计算：x-y
左斜线点计算：x+y

'''

# 记录覃超老师写法

# class Solution:
#     def solveNQueens(self, n: int):
#         if n == 0:
#             return []
#         self.result = []

#         self.cols = set()
#         self.pie = set()
#         self.na = set()
#         self.DFS(n,0,[])
#         return self.getBoard(n)
        
    
#     def DFS(self, n, row, curState):
#         if row == n:
#             self.result.append(curState)
#             return
        
#         for col in range(n):
#             if col in self.cols or row+col in self.na or row-col in self.pie:
#                 continue
            
#             self.cols.add(col)
#             self.na.add(row+col)
#             self.pie.add(row-col)

#             self.DFS(n, row+1, curState+[col])


#             self.cols.remove(col)
#             self.na.remove(row+col)
#             self.pie.remove(row-col)
    
#     def getBoard(self, n):
#         board = []
#         for res in self.result:
#             for i in res:
#                 board.append("." * i + "Q" + "." * (n-i-1))
#         return [board[i:i+n] for i in range(0, len(board), n)]

# 参考国际站简洁写法
# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms

'''
递归遍历行
进入新的行，for loop遍历列，计算当前行位置与每列位置的关系，与上个记录的关系对比
'''
class Solution:
    def solveNQueens(self, n: int):
        def DFS(queens, xyDiff, xySum):
            row = len(queens)
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                if col not in queens and row-col not in xyDiff and row+col not in xySum:
                    DFS(queens+[col], xyDiff+[row-col], xySum+[row+col])
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
# @lc code=end

