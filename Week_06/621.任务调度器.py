# @before-stub-for-debug-begin
from python3problem621 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode-cn.com/problems/task-scheduler/description/
#
# algorithms
# Medium (51.15%)
# Likes:    405
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 66.8K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26
# 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
# 
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 
# 你需要计算完成所有任务所需要的最短时间。
# 
# 
# 
# 示例 ：
# 
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# ⁠    在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
# 
# 
# 提示：
# 
# 
# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。
# 
# 
#
'''
方便理解题解
https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
'''
# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # 记录每个任务出现的次数
        taskMap = dict()
        for task in tasks:
            taskMap[task] = taskMap.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        taskSort = sorted(taskMap.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        maxTaskCount = taskSort[0][1]
        # 至少需要的最短时间
        res = (maxTaskCount - 1) * (n + 1)
        
        for sort in taskSort:
            if sort[1] == maxTaskCount:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))
# @lc code=end

