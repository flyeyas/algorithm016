# @before-stub-for-debug-begin
from python3problem55 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (41.14%)
# Likes:    855
# Dislikes: 0
# Total Accepted:    159.8K
# Total Submissions: 388.3K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
'''
倒着走
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        endIndex = len(nums) - 1
        # 倒转nums索引
        for index in range(len(nums))[::-1]:
            # 检查nums的步数加上当前位置是否能跳到目标位置，如果可以跳转到就继续检查当前索引
            if nums[index] + index >= endIndex:
                endIndex = index
        return not endIndex

'''
国际站写法
https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
正着走，m = i+n 表示能到达的最大索引，一旦下一个数字在的索引大于m, 就无法跳过去
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

# @lc code=end

