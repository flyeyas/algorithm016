# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.19%)
# Likes:    1320
# Dislikes: 0
# Total Accepted:    181.1K
# Total Submissions: 237.6K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start

'''
要点：抛弃人肉递归，寻找重复性，拆解为重复子问题
思路：
    1、输出所有可能性组合
    2、寻找重复性,对称性:
        左侧括号必须要有一个对称的右侧括号，
        左侧括号数量==右侧括号数量，即生成的字符串是一个2n的长度
        每次递归，需要左括号数量 < n, 有括号数量 < 左括号数量
'''
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        strList = []
        self._generateParenthesis(strList, n,'',0,0)
        return strList

    def _generateParenthesis(self, strList: list, n: int, s: str, left:int, right:int):
        # 递归终止层
        if len(s) == n*2:
            strList.append(s)
            return

        # 逻辑层
        if left < n:
            self._generateParenthesis(strList, n, s+'(',left+1, right)
        if right < left:
            self._generateParenthesis(strList, n, s+')',left, right+1)
        
        # 不需要清除逻辑
            
# @lc code=end

