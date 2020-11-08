#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.73%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    85.6K
# Total Submissions: 175.8K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start
'''
2 的幂二进制表示只含有一个 1。
x & (x - 1) 操作会将 2 的幂设置为 0，因此判断是否为 2 的幂是：判断 x & (x - 1) == 0。
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)

# @lc code=end

