#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (34.05%)
# Likes:    1066
# Dislikes: 0
# Total Accepted:    111.6K
# Total Submissions: 327.7K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0       
        stack=[-1,]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i,ch in enumerate(s):
            if '('==ch :  
                stack.append(i)
            elif len(stack) > 1 :  # 右括号，且有成对左括号
                stack.pop()     # 成对匹配
                ans = max(ans, i - stack[-1])
            else:   # 非法的右括号
                stack[0]=i
        return ans
# @lc code=end

