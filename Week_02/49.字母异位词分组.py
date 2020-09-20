# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
import collections
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (63.38%)
# Likes:    464
# Dislikes: 0
# Total Accepted:    105.7K
# Total Submissions: 166.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs)==0:
            return []
        map_dict = collections.defaultdict(list)
        for string in strs:
            map_dict[tuple(sorted(string))].append(string)
        return list(map_dict.values())
# @lc code=end

