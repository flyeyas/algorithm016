# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.88%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    211.8K
# Total Submissions: 544.6K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
'''
二分查找法

官方题解
https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        ans, mid, left, right = -1, 1, 1, x
        while left <= right:
            mid = (left+right)//2
            if mid * mid <= x:
                ans = mid
                left = mid + 1 # 向右挪动
            else:
                right = mid - 1 # 向左挪动
        return ans

'''
牛顿迭代法
https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        cur = 1
        while True:
            pre = cur
            cur = (cur + x/cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
# @lc code=end

