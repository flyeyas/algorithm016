#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.42%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    173.4K
# Total Submissions: 534.8K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
二叉树搜索树的特性：
1、左子树的节点值小于根节点值
2、右子树的节点值大于根节点值
3、由1、2可知二叉搜索树中的子树也符合以上两点特性
4、二叉搜索树的中序遍历是升序的
'''


'''
递归思路：
遍历二叉树，
对比左子树节点值和根节点值大小, 
对比右子树节点值和根节点值大小，

校验左子树时，校验的节点值 小于 父节点，大于左侧子节点，所以： lowerNum应该传递子节点值，upperNum传递父节点值

校验右子树时，校验的节点值 大于 父节点，小于右侧子节点：所以： lowerNum应该传递父节点值，upperNum传递子节点值

修改：

校验左子树时，只需校验子节点是否小于父节点,upperNum = root.val
校验右子树时，只需校验子节点是否大于父节点,lowerNum = root.val

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkTree(root, None, None)
    
    def checkTree(self, root, lowerNum, upperNum):
        if not root:
            return True

        if lowerNum != None and lowerNum >= root.val:
            return False
        
        if upperNum != None and upperNum <= root.val:
            return False
        
        
        # root.val 是父节点

        # 校验左子树时，upperNum = root.val

        # 校验右子树时，lowerNum = root.val
        if not self.checkTree(root.left, lowerNum, root.val):
            return False
        
        if not self.checkTree(root.right, root.val, upperNum):
            return False

        return True

# 递归优化写法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkTree(root)
    
    # inf 表示无穷大值
    def checkTree(self, root, lowerNum =  float('-inf'), upperNum =  float('inf')):
        if not root:
            return True

        if lowerNum >= root.val or upperNum <= root.val:
            return False
        
        if not self.checkTree(root.left, lowerNum, root.val):
            return False
        
        if not self.checkTree(root.right, root.val, upperNum):
            return False

        return True

'''
中序遍历：
中序遍历的顺序：左-根-右
维护一个栈，栈的特性：后进先出
遍历二叉树,
先把根节点入栈，再依次左子树节点入栈，完成后左子树节点弹出，左子树弹出完成后，在弹出根节点，
再去遍历右子树，重复入栈出栈操作
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stackList = []
        inorder = float('-inf')
        while root or stackList:
            while root:
                stackList.append(root)
                root = root.left
            root = stackList.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
    
# @lc code=end

