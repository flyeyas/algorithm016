
# @before-stub-for-debug-begin
# from python3problem26 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 0:
            return 0
        i = 0
        for j in range(1, numsLen):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1
