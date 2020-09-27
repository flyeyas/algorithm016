# @before-stub-for-debug-begin
from python3problem106 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.51%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    58.8K
# Total Submissions: 83.4K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
前序遍历：根-左-右
中序遍历：左-根-右
后续遍历：左-右-根

根据后续遍历获取根节点以及每个子树的父节点

根据中序遍历构造左子树和右子树
左子树list： index_left 到 index-1
右子树list: index+1 到 index_right
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):

            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        if not inorder or not postorder:
            return []
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
# @lc code=end

