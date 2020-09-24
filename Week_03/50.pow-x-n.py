# @before-stub-for-debug-begin
from python3problem50 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (36.66%)
# Likes:    499
# Dislikes: 0
# Total Accepted:    128.2K
# Total Submissions: 349.6K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
'''
暴力方式，循环遍历
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = 1
        for index in range(n):
            num = x*num
        return num

'''
递归：
采用分治方式，进行拆分
思路：
1、计算x的n次方，先递归计算出y 等于 x的(n/2)次方，如果n小于0，就去当前数的倒数
2、根据计算结果，当n为偶数时，x的n次方等于y*y， 当n为基数时，x的n次方等于y*y*x
3、n=0时，x的n次方为1， 任何数的0次方，结果都为1

代码出错地方：递归n时， n/2需要向下取整
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.getNum(x, n) if n>=0 else 1.0/self.getNum(x, -n)
    
    def getNum(self, x, n):
        if n == 0:
            return 1.0
        y = self.getNum(x , n//2)

        return y*y if n%2 == 0 else y*y*x

'''
国际站中的一个递归解法
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
# @lc code=end

